# -*- coding: utf-8 -*-
import json
import logging
from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)

class IndonesiaPaymentController(http.Controller):

    @http.route('/payment/midtrans/webhook', type='json', auth='public', methods=['POST'], csrf=False)
    def midtrans_webhook(self, **post):
        data = json.loads(request.httprequest.data.decode('utf-8'))
        _logger.info("Midtrans Webhook: %s", data)
        tx = request.env['payment.transaction'].sudo().search([('reference', '=', data.get('order_id'))], limit=1)
        if tx:
            tx._process_notification_data({'status': data.get('transaction_status')})
        return {'status': 'OK'}

    @http.route('/payment/xendit/webhook', type='json', auth='public', methods=['POST'], csrf=False)
    def xendit_webhook(self, **post):
        data = json.loads(request.httprequest.data.decode('utf-8'))
        _logger.info("Xendit Webhook: %s", data)
        tx = request.env['payment.transaction'].sudo().search([('reference', '=', data.get('external_id'))], limit=1)
        if tx:
            tx._process_notification_data({'status': data.get('status')})
        return {'status': 'OK'}

    @http.route('/payment/paypal/webhook', type='json', auth='public', methods=['POST'], csrf=False)
    def paypal_webhook(self, **post):
        data = json.loads(request.httprequest.data.decode('utf-8'))
        _logger.info("PayPal Webhook: %s", data)
        resource = data.get('resource', {})
        tx_ref = resource.get('custom_id') or resource.get('invoice_id')
        tx = request.env['payment.transaction'].sudo().search([('reference', '=', tx_ref)], limit=1)
        if tx and data.get('event_type') == 'CHECKOUT.ORDER.APPROVED':
            tx._process_notification_data({'status': 'COMPLETED'})
        return {'status': 'OK'}
