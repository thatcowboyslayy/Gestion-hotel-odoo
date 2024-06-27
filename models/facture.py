from odoo import models, fields, api

class Facture(models.Model):
    _name = 'hotel.facture'
    _description = 'Facture de l\'Hôtel'

    reservation_id = fields.Many2one('hotel.reservation', string='Réservation', required=True)
    date_facture = fields.Date(string='Date de Facture', required=True)
    montant_total = fields.Float(string='Montant Total', compute='_compute_montant_total')

    @api.depends('reservation_id')
    def _compute_montant_total(self):
        for record in self:
            if record.reservation_id.date_fin and record.reservation_id.date_debut:
                delta = record.reservation_id.date_fin - record.reservation_id.date_debut
                record.montant_total = record.reservation_id.chambre_id.prix * delta.days
            else:
                record.montant_total = 0.0
