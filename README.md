# Indonesia Tri-Gateway Payment Acquirers (Midtrans, Xendit, QRIS, PayPal REST v2)

[![License: LGPL-3](https://img.shields.io/badge/License-LGPL--3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![Odoo: 18.0 Community](https://img.shields.io/badge/Odoo-18.0%20Community-purple.svg)](https://www.odoo.com)
[![Price: Free ($0.00)](https://img.shields.io/badge/Price-%240.00%20(Free)-green.svg)](https://airiv.id)
[![Target: Indonesia UMKM / SMB](https://img.shields.io/badge/Market-Indonesia%20%7C%20Cross--Border-red.svg)](https://airiv.id)

A unified, production-ready payment connector built specifically for **Odoo 18 Community Edition**. It provides direct settlement rails for Indonesian domestic commerce (QRIS, E-Wallets, Virtual Accounts, Over-the-Counter retail) and international cross-border transactions (PayPal REST API v2) with **zero external server overhead** and native webhook synchronization.

---

## Detailed Gateway & Payment Channel Features

### 1. QRIS (Quick Response Code Indonesian Standard)
* **National Interoperability**: Compatible with all major Indonesian Mobile Banking apps (BCA Mobile, Livin' by Mandiri, BRImo, BNI Mobile, OCTO Mobile CIMB, BSI Mobile) and E-Wallets (GoPay, OVO, DANA, ShopeePay, LinkAja).
* **Dynamic QR Code Generation**: Automatically embeds the exact invoice payable amount into the generated QR string, preventing reconciliation mismatches from over/underpayments.
* **Dual-Gateway Routing**: Flexible routing allowing merchants to process QRIS via either Midtrans Snap or Xendit Invoicing depending on transaction fee tiers.
* **Instant Reconciliation**: Scanned QRIS payments immediately trigger transaction state transitions from `Draft`/`Pending` to `Done` with automated payment entry creation.

### 2. Midtrans Gateway (Snap / Core API)
* **Dynamic QRIS & Digital Wallets**: Native pop-up and redirect checkout for QRIS, GoPay, and ShopeePay.
* **Virtual Account (VA) Networks**: Automated single-use VA generation for BCA, Bank Mandiri, BNI, BRI, and PermataBank.
* **Credit & Debit Cards**: 3D-Secure transaction flow supporting Visa, Mastercard, JCB, and American Express with recurring card tokenization.
* **Retail Over-The-Counter (OTC)**: Barcode/payment-code generation for over-the-counter payments at Indomaret and Alfamart nationwide.
* **Direct Webhook Controller**: HTTP endpoint at `/payment/midtrans/webhook` captures `settlement`, `pending`, `deny`, `expire`, and `cancel` events directly inside Odoo without middleware.

### 3. Xendit Gateway (Invoicing & Checkout Engine)
* **E-Wallet Direct Integration**: Broad wallet integration covering OVO, DANA, ShopeePay, LinkAja, and AstraPay.
* **Extensive Virtual Account Rails**: Direct bank channels for BCA, Bank Mandiri, BRI, BNI, Bank Syariah Indonesia (BSI), CIMB Niaga, Permata, and Danamon.
* **PayLater & Cardless Credit**: Integrated checkout options for Kredivo and Akulaku consumer installment schemes.
* **Convenience Stores**: Integrated counter payments across the nationwide Alfamart and Indomaret networks.
* **Secure Webhook Verification**: Endpoint at `/payment/xendit/webhook` featuring cryptographic signature validation via Xendit Webhook Verification Token.

### 4. PayPal REST API v2 (Global Cross-Border Settlement)
* **Multi-Currency Processing**: Native settlement for international cross-border sales in USD, EUR, SGD, GBP, AUD, JPY, and other major currencies.
* **Smart Payment Buttons**: Direct client-side popup experience supporting PayPal Wallet, Pay in 4, and international credit cards.
* **REST v2 Orders API**: Direct order capture and instant webhook processing at `/payment/paypal/webhook`.

---

## API Credential Acquisition Guide

### A. Midtrans Setup (Sandbox & Production)
1. Log in to the [Midtrans Merchant Dashboard](https://dashboard.midtrans.com/) (or [Midtrans Sandbox](https://dashboard.sandbox.midtrans.com/) for development).
2. Navigate to **Settings > Access Keys** in the left sidebar.
3. Retrieve your credentials:
   * **Merchant ID** (e.g., `G000000000`)
   * **Client Key** (e.g., `SB-Mid-client-XXXX` or `Mid-client-XXXX`)
   * **Server Key** (e.g., `SB-Mid-server-XXXX` or `Mid-server-XXXX`)
4. Navigate to **Settings > Configuration**:
   * Set **Payment Notification URL** to: `https://your-domain.com/payment/midtrans/webhook`
   * Set **Finish / Unfinish / Error Redirect URLs** to: `https://your-domain.com/payment/status`
   * Save changes.

---

### B. Xendit Setup (Development & Live)
1. Log in to the [Xendit Dashboard](https://dashboard.xendit.co/).
2. Navigate to **Settings > Developers > API Keys**:
   * Click **Generate Secret Key**.
   * Set permissions to **Write** for *Invoices* and *Payments*.
   * Copy the **Secret API Key** (e.g., `xnd_development_...` or `xnd_production_...`).
3. Navigate to **Settings > Developers > Webhooks**:
   * Set the **Invoices Webhook URL** to: `https://your-domain.com/payment/xendit/webhook`
   * Copy the generated **Webhook Verification Token**.
   * Test webhook connectivity using the dashboard simulation tool.

---

### C. PayPal REST API v2 Setup (Sandbox & Live)
1. Log in to the [PayPal Developer Dashboard](https://developer.paypal.com/) with your PayPal Business account.
2. Navigate to **Apps & Credentials** and choose **Sandbox** or **Live**.
3. Click **Create App**, assign an app name (e.g., `Odoo-Tri-Gateway`), and click **Create**.
4. Copy the generated credentials:
   * **Client ID**
   * **Secret Key**
5. (Optional) In **Webhooks**, register `https://your-domain.com/payment/paypal/webhook` and subscribe to `CHECKOUT.ORDER.APPROVED` and `PAYMENT.CAPTURE.COMPLETED`.

---

## Installation & Odoo Configuration

1. **Deploy Module Files**:
   Copy the `airiv_payment_indonesia` directory into your Odoo `custom_addons` directory.

2. **Install Module in Odoo**:
   * Log in to Odoo with Administrator privileges.
   * Enable Developer Mode (`Settings > Activate Developer Mode` or add `?debug=1` to the URL).
   * Go to **Apps > Update Apps List**.
   * Search for `Indonesia Tri-Gateway Payment Acquirers` and click **Activate**.

3. **Configure Acquirers**:
   * Click the top-left **9-dot App Switcher** and open **Indonesian Payments**.
   * Select a provider (**Midtrans**, **Xendit**, or **PayPal REST v2**).
   * Navigate to the **Indonesian Credentials** tab.
   * Enter the corresponding Server/Secret Keys, Client Keys, and Webhook Tokens.
   * Switch the **State** field from `Disabled` to `Test Mode` (or `Enabled` for live transactions).
   * Click **Save**.

---

## Module Specifications

| Specification | Details |
| :--- | :--- |
| **Framework Version** | Odoo 18.0 Community Edition (OWL client compliant) |
| **License** | GNU Lesser General Public License v3.0 (LGPL-3) |
| **Price** | Free ($0.00) |
| **Dependencies** | `payment`, `account` |
| **Server Overhead** | Zero (direct asynchronous controllers, no intermediate servers) |
| **Localization Standard** | Indonesian IDR (Rp), WIB (UTC+7), Tri-Gateway Architecture |
