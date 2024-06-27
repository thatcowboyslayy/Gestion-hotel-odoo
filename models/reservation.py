from odoo import models, fields

class Reservation(models.Model):
    _name = 'hotel.reservation'
    _description = 'Réservation de l\'Hôtel'

    client_id = fields.Many2one('hotel.client', string='Client', required=True)
    chambre_id = fields.Many2one('hotel.chambre', string='Chambre', required=True)
    date_debut = fields.Date(string='Date de Début', required=True)
    date_fin = fields.Date(string='Date de Fin', required=True)
    etat = fields.Selection([('draft', 'Brouillon'), ('confirmed', 'Confirmé'), ('done', 'Terminé'), ('cancelled', 'Annulé')], string='État', default='draft')
