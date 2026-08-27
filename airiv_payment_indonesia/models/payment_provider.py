# -*- coding: utf-8 -*-
from odoo import fields, models

class PaymentProvider(models.Model):
    _inherit = 'payment.provider'

    code = fields.Selection(
        selection_add=[
            ('midtrans', 'Midtrans Payment Gateway'),
            ('xendit', 'Xendit Gateway'),
            ('paypal_rest', 'PayPal REST API v2'),
        ],
        ondelete={'midtrans': 'set default', 'xendit': 'set default', 'paypal_rest': 'set default'}
    )

    midtrans_server_key = fields.Char(string="Midtrans Server Key", groups="base.group_system")
    midtrans_client_key = fields.Char(string="Midtrans Client Key")
    midtrans_merchant_id = fields.Char(string="Midtrans Merchant ID")
    midtrans_is_production = fields.Boolean(string="Midtrans Production Mode", default=False)

    xendit_secret_key = fields.Char(string="Xendit Secret API Key", groups="base.group_system")
    xendit_webhook_token = fields.Char(string="Xendit Webhook Verification Token", groups="base.group_system")

    paypal_rest_client_id = fields.Char(string="PayPal REST Client ID")
    paypal_rest_client_secret = fields.Char(string="PayPal REST Client Secret", groups="base.group_system")
    paypal_rest_environment = fields.Selection([
        ('sandbox', 'Sandbox'),
        ('live', 'Live Production')
    ], string="PayPal REST Environment", default='sandbox')
