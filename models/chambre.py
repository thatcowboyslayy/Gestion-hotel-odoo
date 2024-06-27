from odoo import models, fields

class Chambre(models.Model):
    _name = 'hotel.chambre'
    _description = 'Chambre de l\'Hôtel'

    name = fields.Char(string='Numéro de Chambre', required=True)
    batiment_id = fields.Many2one('hotel.batiment', string='Bâtiment', required=True)
    type_chambre = fields.Selection([('simple', 'Simple'), ('double', 'Double'), ('suite', 'Suite')], string='Type de Chambre', required=True)
    description = fields.Text(string='Description')
    prix = fields.Float(string='Prix par Nuit', required=True)
    image = fields.Binary(string= 'Image')