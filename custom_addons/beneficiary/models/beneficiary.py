from odoo import models, fields, api

class Beneficiary(models.Model):
    _name = 'beneficiary'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Beneficiary'
    _rec_name = 'name_ar'
    active = fields.Boolean(default=True)

    project_number = fields.Integer()
    name_ar = fields.Char(required=1, tracking=1)
    name_fr = fields.Char()
    cin = fields.Char()
    date_of_birth = fields.Char()
    place_of_birth = fields.Char(translate=1)
    birth_certificate_number = fields.Char()
    age = fields.Integer()
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ])
    phone = fields.Char()

    id_number = fields.Char()
    type_of_coverage = fields.Selection([
        ('amo', 'AMO'),
        ('amo_tadamoune', 'AMO TADAMOUNE'),
        ('cnss', 'CNSS'),
        ('amo_p', 'AMO/P'),
        ('amo_d', 'AMO/D'),
        ('cnops', 'CNOPS'),
        ('none', 'None')
    ])
    number_of_registered_family_members = fields.Integer()
    direct_support = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No')
    ])
    presence_of_chronic_disease = fields.Char(translate=1)

    mother_name_fr = fields.Char()
    mother_name_ar = fields.Char()
    mother_cin = fields.Char()
    mother_profession = fields.Char(translate=1)
    mother_employer = fields.Char(translate=1)
    father_name_ar = fields.Char()
    father_name_fr = fields.Char()
    father_cin = fields.Char()
    father_profession = fields.Char(translate=1)
    father_employer = fields.Char(translate=1)
    address = fields.Char(translate=1)

    disability_type = fields.Many2many('disability')
    program_type = fields.Selection([
        ('inclusive_education', 'Inclusive education'),
        ('special_education', 'Special education')
    ])
    subscription_status = fields.Selection([
        ('accepted', 'Accepted'),
        ('waiting_list', 'Waiting list')
    ], default='waiting_list', tracking=1)

    massar_number = fields.Char()
    grade_level = fields.Char(translate=1)
    institution_name = fields.Char(translate=1)

    unit = fields.Char(translate=1)
    section_name = fields.Many2many('section')
    caregiver_name = fields.Many2one('hr.employee')
    technical_component = fields.Many2one('hr.employee')

    occupational_therapy = fields.Many2one('hr.employee')
    speech_therapy = fields.Many2one('hr.employee')
    physical_therapy = fields.Many2one('hr.employee')
    psycho_motor = fields.Many2one('hr.employee')
    psychologist = fields.Many2one('hr.employee')


    line_ids = fields.One2many('beneficiary.line', 'beneficiary_id')



class BeneficiaryLines(models.Model):
    _name = 'beneficiary.line'

    beneficiary_id = fields.Many2one('beneficiary')
    title = fields.Char()
    description = fields.Char()
