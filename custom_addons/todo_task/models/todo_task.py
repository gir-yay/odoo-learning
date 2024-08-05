from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TodoTask(models.Model):
    _name = 'todo.task'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'To do task'
    _rec_name = 'task_name'


    task_name = fields.Char(required=1, tracking=1)
    description = fields.Char(tracking=1)
    due_date = fields.Date(tracking=1)
    estimated_time = fields.Float(required=1)
    total_time_spent = fields.Float(compute='_compute_total', store=1, readonly=0)
    late_task = fields.Boolean()
    status = fields.Selection(
        [
            ('new', 'New'),
            ('in_progress', 'In progress'),
            ('completed', 'Completed'),
            ('closed', 'Closed')
        ], default='new', tracking=1
    )
    assign_to = fields.Many2one('res.partner')
    active = fields.Boolean(default=True)

    line_ids = fields.One2many('todo.task.line', 'todo_task_id')


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

    def action_closed(self):
        for rec in self:
            rec.status = 'closed'

    @api.depends('line_ids.time')
    def _compute_total(self):
        for rec in self:
            rec.total_time_spent = sum(line.time for line in rec.line_ids)

    @api.constrains('total_time_spent', 'estimated_time')
    def _check_total_time_spent(self):
        for rec in self:
            if rec.total_time_spent > rec.estimated_time:
                raise ValidationError('You exceeded the estimated time')

    def check_due_date(self):
        task_ids = self.search([])
        for rec in task_ids:
            if rec.due_date < fields.date.today():
                rec.late_task = True



class TodoTaskLines(models.Model):
    _name = 'todo.task.line'

    todo_task_id = fields.Many2one('todo.task')
    description = fields.Char()
    time = fields.Float(string='Time spent (min)')

