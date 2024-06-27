from odoo import models, fields

class Client(models.Model):
    _name = 'hotel.client'
    _description = 'Client de l\'Hôtel'

    name = fields.Char(string='Nom', required=True)
    email = fields.Char(string='Email')
    telephone = fields.Char(string='Téléphone')
    adresse = fields.Char(string='Adresse')
