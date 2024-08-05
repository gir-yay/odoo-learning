from odoo import models, fields

class ChangeState(models.TransientModel):
    _name = 'change.state'

    property_id = fields.Many2one('property', readonly=1)
    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('pending', 'Pending')
        ], default='draft', required=1
    )
    reason = fields.Char(required=1)

    def action_confirm(self):
        if self.property_id.state == 'closed':
            self.property_id.state = self.state
            self.property_id.create_history_record('closed', self.state, self.reason)

