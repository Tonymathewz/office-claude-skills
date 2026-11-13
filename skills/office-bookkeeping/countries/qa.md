# Qatar (QA) - invoice & bookkeeping profile

> Last checked: 2026-11-13. **Qatar has no VAT yet**, but an e-invoicing law is in progress. Not tax advice: confirm anything important with a Qatari tax adviser or the General Tax Authority (GTA).

## At a glance
| Item | Value |
|---|---|
| Tax name | **No VAT in force.** Corporate income tax, withholding tax and excise (tobacco, sweetened drinks, etc.) exist |
| Tax authority | General Tax Authority (GTA); filings via the Dhareeba portal (dhareeba.gov.qa) |
| Rates | VAT: none. Excise applies to selected goods (volumetric excise on sweetened drinks from 6 Jul 2026) |
| Registration threshold | N/A for VAT. Businesses register with the GTA for income tax / withholding tax |
| Currency | QAR. Financial statements and tax filings in QAR |
| Tax ID name & format | GTA Tax Identification Number (TIN) and Commercial Registration (CR) number. Format not verified - no regex check |
| Online tax-ID check | None found |
| Filing frequency & deadline | Corporate income tax return: 4 months after the accounting year end (usually calendar year). Withholding tax and contract notifications also via Dhareeba |
| Record retention | Accounting books, registers and documents for Qatar activities: **10 years, kept in Qatar** |

## Full tax invoice: required fields
No VAT tax invoice exists. A good commercial invoice (what the skill should expect and issue) shows:
1. The word "Invoice" and a unique sequential number
2. Issue date (and delivery/service date)
3. Supplier legal name, address, CR number (and TIN if the business has one)
4. Customer name and address (CR number for B2B is good practice)
5. Description, quantity, unit price, line totals
6. Discounts, total amount due, currency (QAR or stated foreign currency)
7. Payment terms and bank details
- Excise goods: supplier may show excise-inclusive prices; excise is not reclaimable by an ordinary buyer.

## Simplified invoice / receipt
- No VAT simplified invoice regime. Till receipts are fine as expense evidence; keep them for 10 years.

## Credit and debit notes
- No VAT rules. Good practice: own number, date, reference to the original invoice, reason, amount.

## E-invoicing / clearance status (as of 2026-11-13)
- **Not yet mandatory.** On 6 May 2026 the Council of Ministers approved a draft e-invoicing law and executive regulations (prepared by the Ministry of Finance with the GTA). It still needs Shura Council review and the Amir's approval; not confirmed as published or in force.
- Expected: B2B, B2G and B2C coverage; likely clearance for B2B/B2G and reporting for B2C (similar to Saudi Arabia); phased, larger businesses first. GTA pilot with large entities since late 2025. 1 Jan 2027 has been mentioned but **no date is confirmed**.
- **The skill must NOT fake** any e-invoice number, QR code, UUID or clearance stamp. Re-check this file before each new year; once a mandate starts, issuing must go through the user's certified system.

## Numbering & language
- Use one unique, sequential series for sales invoices.
- Arabic is mandatory for GTA correspondence and for financial statements (years from 1 Jan 2020). English invoices are common in practice; keep Arabic in mind for documents given to the GTA.

## Reverse charge, imports & cross-border
- No VAT reverse charge.
- Payments to non-residents for services in Qatar may require **withholding tax** and contract notification to the GTA: flag `ASK ACCOUNTANT` for every foreign service invoice.
- Imports: customs duty and possibly excise at the border; keep customs declarations.

## Checks the skill must run for this country
- No VAT should appear on an invoice from a Qatari supplier. If a Qatari supplier charges "VAT", flag `CHECK - Qatar has no VAT`.
- Invoice has number, date, supplier name and CR/TIN, description, amount and currency; list missing items.
- Arithmetic: lines add up to total.
- Foreign supplier invoice for services: flag `ASK ACCOUNTANT - withholding tax / contract notification?`
- Sales invoices: sequential numbering, no gaps; never add a VAT line.
- Keep all source documents for 10 years (warn before any archive clean-up).
- Before issuing in 2027 or later: confirm whether the e-invoicing law is in force; if yes, the user must issue through the approved system.

## Common mistakes
- Applying Saudi/UAE VAT logic to Qatari invoices.
- Missing withholding tax on payments to foreign service providers.
- Discarding records after 5 years (Qatar requires 10).

## Sources
- https://www.fiscal-requirements.com/news/5769-qatar-vat-status
- https://www.ey.com/en_gl/technical/tax-alerts/qatar-approves-draft-e-invoicing-law-and-implementing-regulations
- https://www.pwc.com/m1/en/tax/documents/2026/gcc-indirect-tax-news-roundup-q3-2026.pdf
- https://taxsummaries.pwc.com/qatar/corporate/tax-administration
- https://www.wafeq.com/en-qa/business-hub/for-business/accounting-and-compliance-requirements-in-qatar

## Confidence notes
- No GTA (gta.gov.qa / dhareeba.gov.qa) page was read directly.
- Whether the e-invoicing law has been promulgated after May 2026 is unknown; dates are speculative.
- VAT: GCC agreement allows Qatar to introduce 5% VAT; no confirmed date (one blog suggests 2026-2027 but nothing official).
- Commercial invoice fields are good practice, not taken from Qatari law.
- TIN/CR formats and withholding tax rates not verified.
