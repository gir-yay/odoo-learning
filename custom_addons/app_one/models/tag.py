from odoo import fields , models

class Tag(models.Model):
    _name = 'tag'
    name = fields.Char()