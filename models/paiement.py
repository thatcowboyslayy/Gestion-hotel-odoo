from odoo import models, fields

class Paiement(models.Model):
    _name = 'hotel.paiement'
    _description = 'Paiement de l\'Hôtel'

    reservation_id = fields.Many2one('hotel.reservation', string='Réservation', required=True)
    montant = fields.Float(string='Montant', required=True)
    date_paiement = fields.Date(string='Date de Paiement', required=True)
    methode_paiement = fields.Selection([('cash', 'Espèces'), ('credit_card', 'Carte de Crédit'), ('bank_transfer', 'Virement Bancaire')], string='Méthode de Paiement', required=True)
