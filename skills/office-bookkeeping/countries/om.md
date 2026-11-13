# Oman (OM) - invoice & bookkeeping profile

> Last checked: 2026-11-13. Rules change often (Fawtara e-invoicing starts 2027). Not tax advice: confirm anything important with an Omani tax adviser or the Oman Tax Authority (OTA).

## At a glance
| Item | Value |
|---|---|
| Tax name | VAT (Royal Decree 121/2020; Executive Regulations Decision 53/2021, as amended) |
| Tax authority | Oman Tax Authority (OTA), taxoman.gov.om (official site; not opened for this file) |
| Rates | 5% standard (since 16 Apr 2021); 0% (certain basic foods, medicines, international transport, exports, oil/gas); exempt (healthcare, education, some financial services, residential rent). No reduced rate |
| Registration threshold | Mandatory above OMR 38,500 supplies (look-back or look-ahead); voluntary above OMR 19,250; non-GCC non-residents: no threshold |
| Currency | Invoice may be in any currency, but **VAT due must be shown in OMR**, converted at the Central Bank of Oman rate on the tax due date. OMR has 3 decimals (1 OMR = 1,000 baisa) |
| Tax ID name & format | VATIN. Format not officially published (commonly seen as `OM` + 10 digits); soft check regex `^OM\d{10}$` |
| Online tax-ID check | OTA VATIN validation: tms.taxoman.gov.om/portal/vatin-validation (as reported by LookupTax) |
| Filing frequency & deadline | Quarterly (calendar quarters); return and payment due within 30 days after quarter end, online |
| Record retention | 10 years after the end of the tax year in which the return is filed; 15 years for real estate |

## Full tax invoice: required fields
1. The words "Tax Invoice"
2. Issue date, supply date, and payment date (if paid before invoice/supply)
3. Serial number
4. Supplier name, address and VATIN
5. Customer name, address and VATIN (if any) - **often missed**
6. Description of goods/services
7. Quantity of goods
8. Date of any advance payment
9. Total consideration excluding VAT
10. VAT rate applied
11. Discounts, reductions or state subsidies not already deducted
12. Taxable value
13. VAT amount due, in OMR - **often missed on foreign-currency invoices**
- Issue within 15 days of the event (supply or advance payment).
- Summary tax invoice: one invoice for all supplies to the same customer in a calendar month, issued within 15 days after month end, same contents.

## Simplified invoice / receipt
- Allowed only under conditions in the Executive Regulations: supply value below OMR 500 excluding VAT (one source), and OTA approval may be needed (another source). See confidence notes.
- Minimum fields: invoice date, supplier VATIN, taxable amount, VAT rate, VAT charged.
- Not a safe basis for a business input VAT claim; ask for a full tax invoice.

## Credit and debit notes
- Correct an invoice by an amending document that references the original invoice and states the VAT adjustment.
- If the original was electronic, the correction must also be electronic (Exec. Reg. Art. 155).

## E-invoicing / clearance status (as of 2026-11-13)
- **System:** Fawtara. Five-corner model: accredited service providers (ASPs) validate and exchange invoices; tax data reported to the OTA. Structured XML to the **PINT OM** specification (UUIDv5 identifiers, QR code).
- **Legal basis:** OTA Decision 189/2026 (9 Aug 2026) amending the VAT Executive Regulations.
- **Dates:**
  | Group | Mandatory from |
  |---|---|
  | Pilot (~100 large taxpayers) | Aug-Oct 2026, voluntary |
  | Annual supplies > OMR 5m | **1 Apr 2027** |
  | Annual supplies <= OMR 5m (incl. SMEs) | **1 Oct 2027** |
  | Government bodies as issuers | not set by the decision |
- **Scope:** B2B, B2G **and B2C** on the same dates (paper B2C receipts may still be given alongside the electronic invoice). Once the duty applies, paper, PDF and emailed images no longer count as tax invoices.
- OTA's own FAQ showed the older schedule (Feb 2027 / Aug 2027) as of Aug 2026; the decision prevails.
- **The skill must NOT fake** UUIDs, QR codes, ASP validation or OTA reporting status. After go-live, sales invoices must come from the user's ASP-connected system; the skill only prepares data.

## Numbering & language
- Unique serial number per invoice; under Fawtara each invoice also gets a unique electronic identifier.
- Arabic is the official language; English invoices are accepted if an Arabic translation can be provided to the OTA on request.

## Reverse charge, imports & cross-border
- Services from suppliers with no GCC residence: the Omani customer self-accounts VAT (VAT Law Art. 20).
- Imports of goods: VAT at import (deferral scheme may apply); keep customs documents.

## Checks the skill must run for this country
- Document titled "Tax Invoice"; required fields 1-13 above present (list any missing).
- Supplier VATIN present; if not `^OM\d{10}$` mark `CHECK` (not fail).
- Buyer VATIN shown when we are VAT-registered and want to recover VAT.
- VAT rate is 5% or 0%; VAT = taxable value x 5%, rounded to the nearest baisa (0.001 OMR) at line level.
- Foreign-currency invoice: VAT amount shown in OMR.
- Invoice date within 15 days of supply/advance payment where both shown; else note.
- Purchase dated on/after the supplier's Fawtara go-live (1 Apr or 1 Oct 2027) and only a PDF/paper copy: flag `ASK ACCOUNTANT - e-invoice needed?`
- Credit note references an original invoice in the register.
- Foreign supplier, no VAT: flag reverse charge; `ASK ACCOUNTANT` if unsure.

## Common mistakes
- VAT shown only in USD/AED, not OMR.
- Missing supply date or advance-payment date.
- Treating a simplified receipt as a full tax invoice.
- Assuming SMEs are outside Fawtara: all VAT-registered businesses are in from 1 Oct 2027.

## Sources
- https://www.comarch.com/trade-and-services/data-management/legal-regulation-changes/oman-revises-mandatory-e-invoicing-implementation-timeline/
- https://www.alvarezandmarsal.com/node/97951
- https://www.pwc.com/m1/en/tax/documents/2026/gcc-indirect-tax-news-roundup-q3-2026.pdf
- https://invoicedataextraction.com/blog/oman-vat-invoice-requirements
- https://www.deloitte.com/middle-east/en/services/tax/perspectives/oman-issues-its-vat-executive-regulations.html
- https://lookuptax.com/docs/country/oman

## Confidence notes
- No taxoman.gov.om page was read directly; OTA FAQ dates differ from Decision 189/2026.
- VATIN format is not officially published; the `OM` + 10 digits pattern is unverified.
- Simplified invoice: OMR 500 threshold (secondary blog) vs "requires OTA approval" (Deloitte on the 2021 regulations). Confirm before relying on either.
- No e-invoicing penalty schedule published; no grace period announced.
- Zero-rated/exempt examples indicative only.
