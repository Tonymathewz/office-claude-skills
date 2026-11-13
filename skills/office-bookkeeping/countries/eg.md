# Egypt (EG) - invoice & bookkeeping profile

> Last checked: 2026-11-13. Rules change often (e-receipt phases keep expanding). Not tax advice: confirm anything important with an Egyptian accountant or the Egyptian Tax Authority (ETA).

## At a glance
| Item | Value |
|---|---|
| Tax name | VAT (Law 67/2016) plus Table/Schedule tax (ضريبة الجدول) on listed goods/services |
| Tax authority | Egyptian Tax Authority (ETA), eta.gov.eg (official site; not opened for this file) |
| Rates | 14% standard; 5% on machinery/equipment used in production (and medical devices from 29 Jul 2026); 0% exports; exempt list; Table tax separate and **not creditable** |
| Registration threshold | EGP 500,000 combined taxable + exempt sales in any 12 months (apply within 30 days); no threshold for importers for trade, exporters, agents and Table-tax dealers; non-resident digital suppliers above EGP 500,000 |
| Currency | EGP |
| Tax ID name & format | Tax Registration Number (TRN), 9 digits (unofficial). Soft check regex `^\d{9}$` |
| Online tax-ID check | ETA e-services / obligated-taxpayer inquiry (URL not verified) |
| Filing frequency & deadline | Monthly by default, due within the month after the period (pay on filing). Quarterly for turnover up to EGP 20m under Law 6/2025. Nil returns required |
| Record retention | 5 years after the tax period of the return (records kept in Egypt) |

## Full tax invoice: required fields
B2B and B2G invoices must be **ETA e-invoices** (JSON/XML, digitally signed, cleared by ETA). Content:
1. Serial number and issue date (UTC date-time in the e-invoice)
2. Seller name, address, TRN, branch/activity code
3. Buyer name, address, TRN if registered - **often missed**; buyer national ID for individuals above EGP 25,000 (see confidence notes)
4. Item description with GS1 or EGS item code - **often missed**
5. Quantity, unit price, value, discounts
6. VAT and/or Table tax rate and amount
7. Total
8. ETA-assigned **UUID** (and the signed document status "Valid")

## Simplified invoice / receipt
- B2C sales use **ETA e-receipts** (MoF Decision 230/2022), phased by ETA decisions naming taxpayers (phase 9 started Nov 2025).
- Printed e-receipt shows seller name, branch, TRN, date-time, items, tax, total, payment method, **UUID and QR code**.
- Buyer ID (national ID and name) required for an individual buyer when the receipt total is EGP 150,000 or more.
- Offline-issued receipts must be submitted to ETA within 24 hours.
- **E-receipts do not support an input VAT claim**; a business buyer needs an e-invoice.

## Credit and debit notes
- Issued as e-documents through the ETA system, linked to the original e-invoice by its UUID.
- Corrected e-receipts get a new UUID with `referenceOldUUID` pointing to the invalid one.

## E-invoicing / clearance status (as of 2026-11-13)
- **E-invoice (B2B/B2G):** mandatory for all ETA-registered VAT businesses since 15 Dec 2022 (ETA Decision 323/2022). Clearance model: invoice is signed with an electronic seal (USB token or HSM from an approved provider), sent to the ETA portal/API, validated, and given a UUID.
- **Paper or non-validated invoices are not valid for input VAT deduction**, and non-compliance can lead to loss of deductions, fines, and exclusion from public tenders.
- **E-receipt (B2C):** in force for taxpayers named in phase decisions; scope depends on ETA lists, not turnover. Check the business's status with the ETA inquiry using its TRN.
- **The skill must NOT fake** UUIDs, QR codes, electronic signatures/seals or ETA validation status. It may only check they are present on received documents. All sales invoices/receipts must be issued from the user's ETA-integrated system; the skill only prepares data.

## Numbering & language
- Serial numbering by issue date; no erasures. The ETA system assigns the UUID.
- Language for domestic invoices not confirmed; Arabic is customary, e-documents are structured data.

## Reverse charge, imports & cross-border
- B2B services from non-resident suppliers: the Egyptian registered customer self-accounts VAT, paying within 30 days of the supply date.
- Imports of goods: VAT at customs; keep customs declaration.
- Exports: zero-rated; issue an export e-invoice through the ETA system.

## Checks the skill must run for this country
- Every purchase invoice from an Egyptian VAT-registered supplier for which VAT is to be claimed has an **ETA UUID** (and ideally a "Valid" status printout/QR). Missing UUID = flag `NOT CLAIMABLE UNTIL E-INVOICE RECEIVED`.
- Supplier TRN present; if not 9 digits mark `CHECK`.
- Our TRN shown as buyer on B2B purchase invoices.
- VAT rate is 14%, 5% or 0%; VAT = net x rate (0.01 rounding per line). Table tax shown separately and booked as cost, not input VAT.
- E-receipt (B2C-style) used for a business purchase: flag `VAT NOT CLAIMABLE - ask supplier for e-invoice`.
- E-receipt total >= EGP 150,000 to an individual: buyer name and national ID present.
- Credit/debit note references the original invoice UUID.
- Sales: never produce a final invoice for sending; tell the user to issue it from their ETA system. Record the UUID returned in the sales register.
- Foreign service supplier, no VAT: flag reverse charge (pay within 30 days); `ASK ACCOUNTANT` if unsure.

## Common mistakes
- Claiming input VAT on paper/PDF invoices without an ETA UUID.
- Missing item codes (GS1/EGS) causing rejections.
- Confusing Table tax with VAT.
- Missing the 30-day reverse charge payment on foreign services.

## Sources
- https://vatit.com/e-invoicing-guide/egypt/
- https://invoicedataextraction.com/blog/egypt-electronic-receipt-compliance-guide
- https://www.avalara.com/us/en/vatlive/country-guides/africa-and-middle-east/egypt-vat/egyptian-e-invoicing.html
- https://www.cleartax.com/eg/en/e-invoicing-egypt
- https://lookuptax.com/docs/country/egypt-vat-guidelines-indirect-tax
- https://lookuptax.com/docs/tags/egypt

## Confidence notes
- No eta.gov.eg page was read directly; all points come from secondary sources.
- TRN 9-digit format is not confirmed by an official ETA page.
- Buyer national ID threshold on e-invoices (EGP 25,000, from 1 Aug 2024) from one secondary source; e-receipt EGP 150,000 rule from another.
- Submission and cancellation/rejection windows for e-invoices not confirmed (sources say "real time"; one says up to 7 days, phasing out). Not used in checks.
- Later e-receipt phases after Nov 2025 not reviewed.
- Retention: 5 years per two secondary sources; other Egyptian laws may require longer. Ask the accountant.
