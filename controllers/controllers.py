from odoo import http
from odoo.http import request

class HotelReservationController(http.Controller):

    @http.route('/reservation', type='http', auth="public", website=True)
    def reservation_form(self, **kwargs):
        return http.request.render('gestion_hotel.reservation_form_template', {})

    @http.route('/reservation/submit', type='http', auth="public", website=True, csrf=True)
    def reservation_submit(self, **kwargs):
        values = {
            'client_id': kwargs.get('client_id'),
            'chambre_id': kwargs.get('chambre_id'),
            'date_debut': kwargs.get('date_debut'),
            'date_fin': kwargs.get('date_fin'),
        }
        request.env['hotel.reservation'].sudo().create(values)
        return http.request.redirect('/thank-you')
