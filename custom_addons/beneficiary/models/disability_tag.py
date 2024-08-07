from odoo import fields, models

class DisabilityTag(models.Model):
    _name = 'disability'
    name = fields.Char(translate=1)
