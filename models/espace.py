from odoo import models, fields

class Espace(models.Model):
    _name = 'hotel.espace'
    _description = 'Espace de l\'Hôtel'

    name = fields.Char(string='Nom', required=True)
    description = fields.Text(string='Description')
    prix_location = fields.Float(string='Prix de Location', required=True)
    image = fields.Binary(string= 'Image')