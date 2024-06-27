from odoo import models, fields

class Batiment(models.Model):
    _name = 'hotel.batiment'
    _description = 'Bâtiment de l\'Hôtel'

    name = fields.Char(string='Nom', required=True)
    adresse = fields.Char(string='Adresse')
    nbr_chambre = fields.Char(string='Nombre de chambres')
    description = fields.Text(string='Description')
    image = fields.Binary(string= 'Image')
