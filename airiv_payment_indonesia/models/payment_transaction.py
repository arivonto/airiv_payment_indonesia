# -*- coding: utf-8 -*-
from odoo import models, fields

class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    indonesia_payment_channel = fields.Char(string="Payment Channel (QRIS/VA/E-Wallet)")
    gateway_reference = fields.Char(string="Gateway Transaction Reference")

    def _process_notification_data(self, notification_data):
        super()._process_notification_data(notification_data)
        if self.provider_code not in ['midtrans', 'xendit', 'paypal_rest']:
            return
        status = notification_data.get('status')
        if status in ['settlement', 'capture', 'COMPLETED', 'PAID']:
            self._set_done()
        elif status in ['pending', 'PENDING']:
            self._set_pending()
        elif status in ['deny', 'cancel', 'expire', 'EXPIRED', 'FAILED']:
            self._set_canceled()
