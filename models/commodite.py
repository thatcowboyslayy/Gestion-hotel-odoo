from odoo import models, fields

class Commodite(models.Model):
    _name = 'hotel.commodite'
    _description = 'Commodité de l\'Hôtel'

    confort = fields.Char(string='Comfort', required=True)
    divertissement = fields.Char(string='Divertissement')
    service = fields.Char(string='Service')


