from odoo import models, fields

class Planning(models.Model):
    _name = 'hotel.planning'
    _description = 'Planning de l\'Hôtel'

    staff_id = fields.Many2one('hotel.staff', string='Personnel', required=True)
    date = fields.Date(string='Date', required=True)
    shift = fields.Selection([('morning', 'Matin'), ('afternoon', 'Après-midi'), ('night', 'Nuit')], string='Shift', required=True)
