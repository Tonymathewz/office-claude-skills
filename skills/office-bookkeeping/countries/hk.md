# Hong Kong (HK) — invoice & bookkeeping profile

> Last checked: 2026-11-13. Rules change often. Not tax advice: confirm anything important with a local accountant or the tax authority.

## At a glance
| Item | Value |
|---|---|
| Tax name | **No VAT, GST or sales tax.** Main business tax: Profits Tax |
| Tax authority | Inland Revenue Department (IRD) — https://www.ird.gov.hk |
| Rates | Profits Tax two-tier: corporations 8.25% on first HK$2m assessable profits, 16.5% above; unincorporated 7.5% / 15%. Only one entity in a connected group gets the two-tier rate. Territorial basis |
| Registration threshold | No indirect-tax registration. Every business must hold a Business Registration (BR) certificate, renewed yearly (or 3-yearly) and displayed at the place of business |
| Currency | Any currency allowed; HKD most common. State the currency on every invoice |
| Tax ID name & format | Business Registration Number (BRN): first 8 digits of the BR certificate number. Regex `^\d{8}$` (strip suffixes). Companies registered from 27 Dec 2023 use the same number as their Unique Business Identifier |
| Online tax-ID check | No free public BRN validator confirmed (see Confidence notes) |
| Filing frequency & deadline | Annual Profits Tax Return, generally issued on the first working day of April, due 1 month later (extensions for represented/e-filers by year-end code) |
| Record retention | **At least 7 years** (s51C Inland Revenue Ordinance); fine up to HK$100,000 for failure |

## Full tax invoice: required fields
There is **no statutory "tax invoice"** and no law prescribing invoice fields. Because there is no VAT, no tax line should appear. Good-practice minimum (the skill should treat as required):
1. Seller legal name (as registered) and address
2. Seller BRN (commonly shown; widely treated as expected)
3. Unique invoice number
4. Invoice date
5. Buyer name and address
6. Description, quantity, unit price
7. Total amount **and currency** (often missed in cross-border work)
8. Payment terms/due date and bank details
Records must let the IRD trace goods/services, parties, quantities and values (s51C).

## Simplified invoice / receipt
- No simplified-invoice regime. Any receipt that evidences the expense (date, payee, amount, what was bought) supports bookkeeping.
- Keep bank/card statements alongside receipts: IRD lists vouchers, bank statements, invoices and receipts as supporting records.

## Credit and debit notes
- No statutory format. Good practice: own unique number, date, reference to the original invoice number, reason, amount and currency.

## E-invoicing / clearance status (as of last-checked date)
- **No B2B e-invoicing mandate and no clearance.** PDF and electronic records are acceptable; IRD has separate guidance on admissibility of electronic records (pamphlet pam60e).
- Nothing to fake here, but the skill must not add a "VAT"/"GST" line to Hong Kong invoices.

## Numbering & language
- Unique, sequential numbering is good practice (supports s51C sufficiency).
- Records must be kept in **English or Chinese**.

## Reverse charge, imports & cross-border
- No reverse charge (no VAT). Overseas supplier invoices are recorded at gross amount.
- Watch for foreign VAT/GST charged by overseas suppliers: it is a cost, not recoverable in HK.
- Foreign-sourced dividends, interest, IP income and disposal gains may be taxable unless FSIE conditions (from 1 Jan 2023) are met — flag to accountant.

## Checks the skill must run for this country
- Issued invoices: no VAT/GST/sales-tax line; if present → error.
- Invoice has unique number, date, seller name, buyer name, description, amount, **explicit currency code**.
- Seller BRN present and 8 digits (warning if missing on sales invoices issued by us).
- Duplicate invoice-number check per supplier.
- Records/language check: document in English or Chinese, else flag for translation note.
- Retention reminder: do not delete any record younger than 7 years.
- Received invoice from abroad showing foreign VAT → book as cost, not as recoverable tax.
- Month-end: bank reconciliation completed and supporting docs for every bank line (supports "sufficient records").

## Common mistakes
- Adding "VAT 0%" or copying a UK/EU template with tax lines.
- Missing currency (HKD vs USD vs RMB) on cross-border invoices.
- Throwing away daily cash records/receipts because the bank statement exists.
- Assuming offshore income is automatically tax-free.

## Sources
- https://ird.gov.hk/eng/tax/bus_rke.htm (IRD record keeping, s51C, 7 years, HK$100,000 fine, English or Chinese)
- https://www.ird.gov.hk/eng/pdf/pam56e.pdf (IRD guide to Profits Tax: 7-year record rule, returns)
- https://www.hawksford.com/insights-and-guides/taxation-and-accounting-in-hong-kong (no VAT/GST, two-tier rates, return timing, FSIE)
- https://getstarted.hk/business-registration-br-number-vs-company-registration-cr-number/ (BRN = first 8 digits, display, renewal, UBI)
- https://invoicedataextraction.com/blog/hong-kong-invoice-requirements (no statutory invoice template; good-practice fields; no e-invoicing mandate)

## Confidence notes
- Whether showing the BRN on invoices is legally required is unclear — one secondary source says so without citing a provision; treat as strong good practice.
- Companies Ordinance company-name disclosure rules on invoices not checked.
- No free official BRN validation service confirmed (IRD BR search/ Companies Registry search may charge fees) — not verified.
- Profits Tax rates per secondary source (Hawksford), not read on IRD site this session.
