from odoo import models, fields, api

class CustomerTurn(models.Model):
    _name = 'customer.turn'
    _description = 'Gestión de Turnos para Atención al Cliente'

    name = fields.Char(string='Turno', required=True)
    customer_name = fields.Char(string='Nombre del Cliente', required=True)
    status = fields.Selection([
        ('waiting', 'En Espera'),
        ('in_progress', 'En Progreso'),
        ('completed', 'Completado')
    ], string='Estado', default='waiting')
    assigned_employee = fields.Many2one('hr.employee', string='Empleado Asignado')
    start_time = fields.Datetime(string='Hora de Inicio')
    end_time = fields.Datetime(string='Hora de Finalización')

    @api.depends('start_time', 'end_time')
    def _compute_duration(self):
        for record in self:
            if record.start_time and record.end_time:
                record.duration = (record.end_time - record.start_time).total_seconds() / 60.0
            else:
                record.duration = 0.0

    duration = fields.Float(string='Duración (minutos)', compute='_compute_duration', store=True)