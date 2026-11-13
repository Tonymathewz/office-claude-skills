# Saudi Arabia (SA) - invoice & bookkeeping profile

> Last checked: 2026-11-13. Rules change often (FATOORA integration waves are still being added). Not tax advice: confirm anything important with a Saudi tax adviser or ZATCA.

## At a glance
| Item | Value |
|---|---|
| Tax name | VAT (ضريبة القيمة المضافة) |
| Tax authority | Zakat, Tax and Customs Authority (ZATCA), https://zatca.gov.sa |
| Rates | 15% standard; 0% (exports, international transport, qualifying medicines/medical equipment, investment metals, etc.); exempt (some financial services, residential rent) |
| Registration threshold | Mandatory above SAR 375,000 taxable supplies in 12 months (actual or expected); voluntary above SAR 187,500; non-residents: no threshold |
| Currency | SAR. Other currencies allowed, but VAT must be shown in SAR, converted at the Saudi Central Bank (SAMA) rate on the tax due date |
| Tax ID name & format | VAT registration number: 15 digits; first digit = GCC state code (3 for KSA). Commonly starts and ends with `3`: soft check regex `^3\d{13}3$` |
| Online tax-ID check | ZATCA website VAT number lookup (URL not verified for this file) |
| Filing frequency & deadline | Monthly if taxable supplies > SAR 40m a year, otherwise quarterly (may opt monthly). Due last day of the month after the period |
| Record retention | 6 years from end of the tax period; 11 years for movable capital asset records; 15 years for real estate |

## Full tax invoice: required fields
Title **"Tax Invoice" / فاتورة ضريبية**, in Arabic (other languages may be added).
1. Issue date **and time**; supply date if different - **time often missed**
2. Sequential invoice number
3. Supplier name, address, VAT number
4. Customer name and address; customer VAT number if registered - **often missed**
5. Per line: description, unit price, quantity, discount, taxable amount, VAT rate, VAT amount, line total incl. VAT
6. Totals in SAR: taxable amount, VAT, total incl. VAT
7. QR code (all e-invoices)
8. Phase 2 (integrated) invoices also carry a UUID, invoice hash and cryptographic stamp in the XML, and are **cleared by ZATCA before** being shared with the buyer
- Issue no later than the 15th day of the month after the month of supply.

## Simplified invoice / receipt
- **Simplified Tax Invoice / فاتورة ضريبية مبسطة**: B2C (sales to individuals not registered for VAT). The older guideline also limits it to supplies under SAR 1,000 (see confidence notes).
- Minimum fields: date, supplier name, address, VAT number, description, total, and either the VAT amount or a statement that the price includes 15% VAT, plus the **QR code**.
- Must be issued at the time of supply or payment, whichever is first.
- A business buyer should not claim input VAT on a simplified invoice; ask the supplier for a standard tax invoice showing the buyer's VAT number.

## Credit and debit notes
- Titled "Credit Note" / "Debit Note" (Arabic), own serial number, **reference to the original tax invoice number**, supply date, reason for adjustment, VAT adjustment.
- Must relate to a prior supply. Under Phase 2, notes go through the same clearance (standard) or reporting (simplified) flow as invoices.

## E-invoicing / clearance status (as of 2026-11-13)
- **System:** FATOORA.
- **Phase 1 (Generation), from 4 Dec 2021:** all resident VAT taxpayers must issue invoices from a compliant electronic solution. Handwritten/manual invoices not allowed. Simplified invoices need a QR code (seller name, VAT number, timestamp, total incl. VAT, VAT amount).
- **Phase 2 (Integration), from 1 Jan 2023 in waves:** solution integrated with ZATCA. ZATCA notifies each wave at least 6 months ahead.
  - Standard (B2B) invoices: sent to ZATCA for **clearance**; only the cleared invoice is valid to share.
  - Simplified (B2C) invoices: **reported** to ZATCA within 24 hours.
  - Each document has a UUID, invoice hash chained to the previous one, and a cryptographic stamp; the QR code carries extra Phase 2 data.
  - Wave 24: VAT revenue > SAR 375,000 (2022-2024), integrate by 30 Jun 2026.
  - **Wave 25: VAT revenue > SAR 187,500 in any of 2022-2025, integrate by 1 Feb 2027.**
- **Prohibited:** deleting or editing issued invoices, duplicate sequence numbers, changing the system clock, exporting the private stamp key.
- **The skill must NOT fake or create:** QR codes, UUIDs, invoice hashes, cryptographic stamps or clearance status. It can only check they are present on received documents. For issuing, tell the user to issue from their ZATCA-compliant (and, if in a wave, integrated) e-invoicing solution; the skill may only prepare the data to type in.

## Numbering & language
- Sequential numbering without gaps or duplicates (the e-invoicing solution generates this).
- **Arabic is mandatory**; bilingual invoices are fine, and the Arabic text prevails.
- Self-billing (customer issues on supplier's behalf) needs a prior agreement and ZATCA approval, and must state it is issued on behalf of the supplier.

## Reverse charge, imports & cross-border
- Services from non-resident suppliers: the Saudi registered customer self-accounts VAT in its return; the foreign supplier does not issue a Saudi tax invoice.
- Imports of goods: VAT paid at customs; keep the customs declaration as evidence.
- Exports and services to non-GCC residents may be zero-rated; keep export evidence.

## Checks the skill must run for this country
- Document is in Arabic (Arabic title present). English-only = flag.
- Supplier VAT number present, 15 digits; if it does not match `^3\d{13}3$` mark `CHECK` (not fail).
- B2B purchase: titled Tax Invoice (not Simplified), shows buyer name, address and **our VAT number**; otherwise not a basis for input VAT, flag.
- **QR code present** on every received invoice dated on/after 4 Dec 2021. Missing = flag. Do not decode-and-trust: say "QR present, not validated".
- Issue date includes a time (e-invoice requirement); missing time = `CHECK`.
- VAT rate is 15% or 0%; VAT = taxable amount x 15% (0.01 rounding per line). VAT amount shown in SAR.
- Credit/debit note references an original invoice number that exists in the purchases/sales register.
- Sales: never produce a "final" invoice PDF for the user to send. If our business is in a Phase 2 wave (or unsure), tell the user to issue it from their integrated solution.
- Foreign supplier, no VAT: flag reverse charge; `ASK ACCOUNTANT` if unsure.

## Common mistakes
- Accepting English-only or handwritten invoices.
- Claiming input VAT from simplified invoices or till receipts.
- Buyer VAT number missing on standard invoices.
- Invoices in USD without the SAR VAT amount.
- Thinking a small business is exempt from integration: Wave 25 reaches businesses with just SAR 187,500 VAT revenue.

## Sources
- https://zatca.gov.sa/en/E-Invoicing/Introduction/Guidelines/Documents/Simplified%20guide_En.pdf
- https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Guideline-for-Tax-Invoicing-and-Records-under-VAT-Provisions.pdf
- https://www.comarch.com/trade-and-services/data-management/legal-regulation-changes/saudi-arabia-announces-wave-25-of-e-invoicing-integration/
- https://noqta.tn/en/news/zatca-wave-25-e-invoicing-threshold-halved-2026
- https://www.pwc.com/m1/en/tax/documents/2026/gcc-indirect-tax-news-roundup-q3-2026.pdf
- https://www.fonoa.com/resources/country-tax-guides/saudi-arabia

## Confidence notes
- VAT number "starts and ends with 3" is common practice, not confirmed on a ZATCA page; Fonoa gives the structure (state digit, serial, check digit, branch, tax type). Treat as a soft check only.
- Simplified-invoice scope: the ZATCA invoicing guideline read says supplies under SAR 1,000 to non-registered individuals; e-invoicing material treats all B2C as simplified. Confirm with the accountant.
- Detailed Phase 2 QR contents (hash, signature, public key) and the hash-chaining rule come from general knowledge of the ZATCA spec, not a page read here.
- Voluntary threshold SAR 187,500 not confirmed on a page read here (it matches the Wave 25 figure, which is a different test).
- Waves after 25 not announced as of 2026-11-13 (none found).
- The ZATCA "What is e-invoicing" page could not be fetched.
