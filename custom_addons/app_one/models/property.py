from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Property(models.Model):
    _name = 'property'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Property'

    # reserved fields
    ref = fields.Char(default='New', readonly=1)
    name = fields.Char(required=1, tracking=1, translate=1)
    active = fields.Boolean(default=True)

    description = fields.Text(size=150, default='new')
    postcode = fields.Char(default='00000')
    date_availability = fields.Date(tracking=1)
    expected_selling_date = fields.Date()
    sold_late = fields.Boolean()
    expected_price = fields.Float(digits=(0, 5))
    selling_price = fields.Float()
    diff = fields.Float(compute='_compute_diff', store=1, readonly=0)
    bedrooms = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('west', 'West'),
        ('east', 'East'),
    ], default='north', required=True)

    owner_id = fields.Many2one('owner')
    tag_ids = fields.Many2many('tag')
    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('pending', 'Pending'),
            ('done', 'Done'),
            ('closed', 'Closed')
        ], default='draft'
    )

    owner_address = fields.Char(related="owner_id.address", readonly=0, store=1)

    line_ids = fields.One2many('property.line', 'property_id')

    _sql_constraints = [
        ('unique_name', 'unique("name")', 'Name already taken')
    ]

    # @api.onchange('view_field_name')
    # _function()

    @api.depends('expected_price', 'selling_price')
    def _compute_diff(self):
        for rec in self:
            rec.diff = rec.expected_price - rec.selling_price

    @api.constrains('expected_price')
    def _check_expected_price_gte_0(self):
        for rec in self:
            if rec.expected_price < 0:
                raise ValidationError('price cannot be negative')

    def action_draft(self):
        for rec in self:
            rec.create_history_record(rec.state, 'draft')
            rec.state = 'draft'

    def action_pending(self):
        for rec in self:
            rec.create_history_record(rec.state, 'pending')
            rec.state = 'pending'

    def action_done(self):
        for rec in self:
            rec.create_history_record(rec.state, 'done')
            rec.state = 'done'

    def action_closed(self):
        for rec in self:
            rec.create_history_record(rec.state, 'closed')
            rec.state = 'closed'

    def check_expected_selling_date(self):
        property_ids = self.search([])
        for rec in property_ids:
            if rec.expected_selling_date < fields.date.today():
                rec.sold_late = True

    # overriding the create function to generate a seq once the new property is saved
    @api.model
    def create(self, vals):
        res = super(Property, self).create(vals)
        if res.ref == 'New':
            res.ref = self.env['ir.sequence'].next_by_code('property_seq')
        return res

    def create_history_record(self, old_state, new_state, reason=""):
        for rec in self:
            rec.env['property.history'].create({
                'user_id': rec.env.uid,
                'property_id': rec.id,
                'old_state': old_state,
                'new_state': new_state,
                'reason': reason or ""

            })

    def action_open_change_state_wizard(self):
        action = self.env['ir.actions.actions']._for_xml_id('app_one.property_change_state_wizard_action')
        action['context'] = {
            'default_property_id': self.id
        }
        return action


    def action_open_related_owner(self):
        action = self.env['ir.actions.actions']._for_xml_id('app_one.owner_action')
        view_id = self.env.ref('app_one.owner_view_form').id
        action['res_id'] = self.owner_id.id
        action['views'] = [[view_id, 'form']]
        return action

class PropertyLines(models.Model):
    _name = 'property.line'

    property_id = fields.Many2one('property')
    area = fields.Float()
    description = fields.Char()
