# -*- coding: utf-8 -*-
{
    'name': 'Indonesia Tri-Gateway Payment Acquirers (Midtrans, Xendit, PayPal)',
    'version': '18.0.1.0.0',
    'category': 'Accounting/Payment Providers',
    'summary': 'Unified Tri-Gateway Payment Engine for Indonesia (Midtrans, Xendit, PayPal v2)',
    'author': 'Riv Cloud Management',
    'website': 'https://airiv.id',
    'license': 'LGPL-3',
    'price': 0.0,
    'currency': 'EUR',
    'depends': ['payment', 'account'],
    'data': [
        'views/payment_provider_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
