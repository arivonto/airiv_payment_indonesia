# Indonesia Tri-Gateway Payment Acquirers

[![Odoo](https://img.shields.io/badge/Odoo-18.0-714B67.svg)](https://www.odoo.com/)
[![License](https://img.shields.io/badge/License-LGPL--3-0f766e.svg)](LICENSE)
[![Author](https://img.shields.io/badge/Author-AIRIV-0891b2.svg)](https://airiv.id)
[![GitHub Actions](https://github.com/arivonto/airiv_payment_indonesia/actions/workflows/odoo-appstore-ci.yml/badge.svg?branch=18.0)](https://github.com/arivonto/airiv_payment_indonesia/actions)
[![Apps Store Ready](https://img.shields.io/badge/Odoo%20Apps%20Store-ready-22c55e.svg)](https://apps.odoo.com/)

AIRIV Payment Indonesia is a unified Odoo 18 Community payment-provider layer for Indonesian domestic commerce and cross-border settlement. It adds Midtrans, Xendit, and PayPal provider options, QRIS and virtual-account settings, transaction payment-channel evidence, and direct webhook routes for payment state synchronization.

## Core Capabilities & Architecture

### Core capabilities

- Tri-gateway provider layer: Midtrans Indonesia, Xendit Indonesia, and PayPal cross-border provider codes.
- Gateway credentials: merchant ID, client/public key, server/secret key, and sandbox/production environment.
- Indonesian channel flags: Dynamic QRIS and virtual-account enablement per provider.
- Transaction evidence: QRIS raw string, virtual-account number, Indonesian payment channel, and gateway transaction reference.
- Direct webhook controllers: Midtrans, Xendit, and PayPal callbacks handled directly by Odoo.
- Transaction state mapping: gateway statuses mapped into Odoo transaction states such as done, pending, and canceled.

### Architecture

```text
Odoo Payment Flow
  |
  |-- payment.provider
  |-- payment.transaction
  |-- customer invoice or checkout
  v
AIRIV Payment Indonesia Layer
  |
  |-- Midtrans provider code
  |-- Xendit provider code
  |-- PayPal cross-border provider code
  |-- gateway credentials
  |-- QRIS and virtual-account flags
  v
Gateway Webhook Controllers
  |
  |-- /payment/midtrans/webhook
  |-- /payment/xendit/webhook
  |-- /payment/paypal/webhook
  v
Odoo Transaction State
  |
  |-- done
  |-- pending
  |-- canceled
  |-- gateway reference evidence
```

## Feature & Workflow Automation

1. Install provider layer
   - Install this module after Odoo Payment and Accounting are available.

2. Configure gateway credentials
   - Fill merchant ID, client/public key, server/secret key, environment, QRIS, and virtual-account options on payment providers.

3. Register gateway webhooks
   - Configure provider dashboards to send payment status notifications to the Odoo callback URLs.

4. Synchronize transaction state
   - Let Odoo map gateway notifications into payment transaction states and preserve channel/reference evidence.

## Technical Specifications

| Item | Detail |
| --- | --- |
| Odoo series | 18.0 |
| Odoo edition | Community |
| Module technical name | `airiv_payment_indonesia` |
| Version | `18.0.1.0.0` |
| License | LGPL-3 |
| Author | AIRIV |
| Category | Accounting/Payment Providers |
| Dependencies | `payment`, `account` |
| Main models | `payment.provider`, `payment.transaction` |
| Provider fields | `id_merchant_id`, `id_client_key`, `id_server_key`, `id_environment`, `id_enable_qris`, `id_enable_va` |
| Transaction fields | `id_qris_qr_string`, `id_va_number`, `id_payment_channel`, `indonesia_payment_channel`, `gateway_reference` |
| Webhook routes | `/payment/midtrans/webhook`, `/payment/xendit/webhook`, `/payment/paypal/webhook` |
| Store assets | `icon.png`, `banner.png`, `index.html` |

## Installation Guidance

1. Clone the repository branch for Odoo 18:

   ```bash
   git clone -b 18.0 https://github.com/arivonto/airiv_payment_indonesia.git
   ```

2. Place the module in your Odoo addons path.

3. Restart Odoo.

4. Activate developer mode if needed.

5. Update the Apps list.

6. Search for `Indonesia Tri-Gateway Payment Acquirers`.

7. Install the module.

## Configuration Checklist

- Confirm Odoo Payment and Accounting are installed.
- Prepare active Midtrans, Xendit, or PayPal Business account credentials.
- Start in sandbox/testing mode before production activation.
- Fill gateway merchant ID, client/public key, and server/secret key.
- Enable QRIS and virtual-account channels only where supported by the selected provider.
- Register gateway webhook URLs:
  - `https://your-domain.com/payment/midtrans/webhook`
  - `https://your-domain.com/payment/xendit/webhook`
  - `https://your-domain.com/payment/paypal/webhook`
- Run a controlled sandbox payment and confirm the Odoo transaction status is updated.

## Repository Layout

```text
airiv_payment_indonesia/
  README.md
  LICENSE
  .github/
    workflows/
      odoo-appstore-ci.yml
    scripts/
      validate_odoo_appstore.py
  airiv_payment_indonesia/
    __manifest__.py
    controllers/
      main.py
    data/
      payment_provider_data.xml
    models/
      payment_provider.py
      payment_transaction.py
    static/
      description/
        icon.png
        icon_128.png
        airiv_store_icon.png
        airiv_store_icon_128.png
        banner.png
        index.html
    views/
      payment_provider_views.xml
  static/
    description/
      icon.png
      icon_128.png
      airiv_store_icon.png
      airiv_store_icon_128.png
      banner.png
      index.html
```

## Contact Info

| Item | Detail |
| --- | --- |
| Author | AIRIV |
| Website | https://airiv.id |
| GitHub | https://github.com/arivonto |
| Module repository | https://github.com/arivonto/airiv_payment_indonesia |
| Odoo series | 18.0 |

## Quality Gate

This repository is prepared for Odoo Apps Store submission with:

- Parseable Odoo manifest metadata.
- Root and module-level documentation.
- Odoo Apps Store description fragment.
- Required store images.
- LGPL-3 license metadata.
- GitHub Actions Apps Store audit on branch `18.0`.

