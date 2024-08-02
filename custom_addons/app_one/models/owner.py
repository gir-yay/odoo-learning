from odoo import fields , models

class Owner(models.Model):
    _name = "owner"
    name = fields.Char(required=1)
    phone = fields.Char()
    address = fields.Char()
    property_ids = fields.One2many('property', 'owner_id')