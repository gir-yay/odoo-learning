from odoo import models, fields, api

class TodoTask(models.Model):
    _name = 'todo.task'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'To do task'
    _rec_name = 'task_name'


    task_name = fields.Char(required=1, tracking=1)
    description = fields.Char(tracking=1)
    due_date = fields.Date(tracking=1)
    status = fields.Selection(
        [
            ('new', 'New'),
            ('in_progress', 'In progress'),
            ('completed', 'Completed')
        ], default='new', tracking=1
    )
    assign_to = fields.Many2one('res.partner')

    _sql_constraints = [
        ('unique_task_name', 'unique("task_name")', 'Task name already taken')
    ]

    def action_new(self):
        for rec in self:
            rec.status = 'new'

    def action_in_progress(self):
        for rec in self:
            rec.status = 'in_progress'

    def action_completed(self):
        for rec in self:
            rec.status = 'completed'


