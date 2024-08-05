from odoo import models, fields, api

class PropertyHistory(models.Model):
    _name = 'property.history'
    _description = 'Property history'

    user_id = fields.Many2one('res.users')
    property_id = fields.Many2one('property')
    date = fields.Date()
    old_state = fields.Char()
    new_state = fields.Char()
    reason = fields.Char()

    @api.model
    def create(self, vals):
        res = super(PropertyHistory, self).create(vals)
        res.date = fields.datetime.today()
        return res
