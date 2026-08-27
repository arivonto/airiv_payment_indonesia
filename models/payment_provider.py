# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class PaymentProviderIndonesia(models.Model):
    _inherit = 'payment.provider'

    code = fields.Selection(
        selection_add=[
            ('midtrans', 'Midtrans Indonesia'),
            ('xendit', 'Xendit Indonesia'),
            ('paypal', 'PayPal Cross-Border'),
        ],
        ondelete={
            'midtrans': 'set default',
            'xendit': 'set default',
            'paypal': 'set default',
        }
    )

    id_merchant_id = fields.Char(string="Merchant ID")
    id_client_key = fields.Char(string="Client / Public Key")
    id_server_key = fields.Char(string="Server / Secret Key")
    id_environment = fields.Selection([
        ('sandbox', 'Sandbox / Testing'),
        ('production', 'Production / Live'),
    ], string="Environment", default='sandbox')
    id_enable_qris = fields.Boolean(string="Enable Dynamic QRIS", default=True)
    id_enable_va = fields.Boolean(string="Enable Virtual Accounts", default=True)


class PaymentTransactionIndonesia(models.Model):
    _inherit = 'payment.transaction'

    id_qris_qr_string = fields.Text(string="QRIS Raw String")
    id_va_number = fields.Char(string="Virtual Account Number")
    id_payment_channel = fields.Char(string="Indonesian Payment Channel")
