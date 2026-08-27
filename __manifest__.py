# -*- coding: utf-8 -*-
{
    'name': 'Indonesia Tri-Gateway Payment Acquirers (Midtrans, Xendit, PayPal)',
    'version': '18.0.1.0.0',
    'category': 'Accounting/Payment Providers',
    'summary': 'Unified Tri-Gateway Payment Engine for Indonesia (Midtrans, Xendit, PayPal v2)',
    'description': """
Indonesia Tri-Gateway Payment Engine for Odoo 18 Community.
- Midtrans Snap & Core API (Dynamic QRIS, Virtual Accounts, Cards, OTC Indomaret/Alfamart)
- Xendit Invoicing (QRIS, OVO, DANA, ShopeePay, LinkAja, PayLater)
- PayPal REST v2 (USD, EUR, SGD Multi-Currency Cross-Border Settlement)
- Direct Webhook Controllers with Zero External Server Overhead
""",
    'author': 'Riv Cloud Management',
    'website': 'https://airiv.id',
    'license': 'LGPL-3',
    'price': 0.0,
    'currency': 'EUR',
    'depends': ['payment', 'account'],
    'data': [
        'views/payment_provider_views.xml',
    ],
    'images': [
        'static/description/banner.png',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
