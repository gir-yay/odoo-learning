from odoo import fields , models

class SectionTag(models.Model):
    _name = 'section'
    name = fields.Char(translate=1)