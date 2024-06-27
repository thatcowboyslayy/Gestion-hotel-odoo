from odoo import models, fields

class Staff(models.Model):
    _name = 'hotel.staff'
    _description = 'Personnel de l\'Hôtel'

    name = fields.Char(string='Nom', required=True)
    poste = fields.Char(string='Poste', required=True)
    telephone = fields.Char(string='Téléphone')
    email = fields.Char(string='Email')
