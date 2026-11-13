# Kuwait (KW) - invoice & bookkeeping profile

> Last checked: 2026-11-13. **Kuwait has no VAT and no excise yet.** Not tax advice: confirm anything important with a Kuwaiti tax adviser or the Ministry of Finance.

## At a glance
| Item | Value |
|---|---|
| Tax name | **No VAT in force.** Corporate income tax on foreign entities, Zakat / NLST / KFAS for certain Kuwaiti companies, Domestic Minimum Top-up Tax for large multinational groups (from 2025) |
| Tax authority | Ministry of Finance (Tax Administration) |
| Rates | VAT: none. Excise: none |
| Registration threshold | N/A for VAT |
| Currency | KWD (3 decimals: 1 KWD = 1,000 fils) |
| Tax ID name & format | No VAT number. Businesses are identified by Commercial Registration / licence number; tax file numbers for taxable entities. Format not verified - no regex check |
| Online tax-ID check | None found |
| Filing frequency & deadline | N/A for VAT. Income tax / Zakat / NLST deadlines: ask the accountant |
| Record retention | Keep accounting records at least **10 years** (commercial and tax law, as reported) |

## Full tax invoice: required fields
No VAT tax invoice exists. A good commercial invoice shows:
1. The word "Invoice" and a unique sequential number
2. Issue date (and delivery/service date)
3. Supplier legal name, address, CR/licence number
4. Customer name and address
5. Description, quantity, unit price, line totals
6. Total amount due and currency (KWD to 3 decimals, or stated foreign currency)
7. Payment terms and bank details
- For contracts with the government or large clients, the contract may require extra details (contract number, PO number).

## Simplified invoice / receipt
- No VAT regime. Receipts are fine as expense evidence; keep for 10 years.

## Credit and debit notes
- No VAT rules. Good practice: own number, date, reference to the original invoice, reason, amount.

## E-invoicing / clearance status (as of 2026-11-13)
- **No e-invoicing mandate and no official announcement** (PwC Q3 2026). VAT is reported to be left out of the 2026-2030 fiscal plan.
- **The skill must NOT fake** any e-invoice number, QR code or stamp. Re-check this file if Kuwait announces VAT or e-invoicing.

## Numbering & language
- One unique, sequential series for sales invoices.
- Arabic and English are both used in practice; no invoice-language rule verified.

## Reverse charge, imports & cross-border
- No VAT reverse charge.
- **5% retention:** government bodies (and, per some sources, companies) withhold 5% of payments to contractors/subcontractors until the contractor shows a Tax Clearance Certificate. Rules updated in March 2026 for DMTT groups. Flag `ASK ACCOUNTANT` when paying contractors or receiving a short payment from a government client.
- Imports: customs duty at the border; keep customs declarations.

## Checks the skill must run for this country
- No VAT should appear on an invoice from a Kuwaiti supplier. If one appears, flag `CHECK - Kuwait has no VAT`.
- Invoice has number, date, supplier name and CR/licence number, description, amount and currency; list missing items.
- KWD amounts use 3 decimals; check arithmetic to 0.001.
- Payment to a contractor/subcontractor under a contract: flag `ASK ACCOUNTANT - 5% retention until tax clearance certificate?`
- Customer payment exactly 5% short on a contract invoice: match it as "retention" in bank reconciliation, not as an unexplained shortfall.
- Sales invoices: sequential, no gaps, no VAT line.
- Keep source documents 10 years.

## Common mistakes
- Treating 3-decimal KWD amounts as 2-decimal (e.g. 12.500 read as 12,500).
- Releasing contractor retentions without a tax clearance certificate.
- Applying GCC VAT logic to Kuwaiti invoices.

## Sources
- https://www.pwc.com/m1/en/tax/documents/2026/gcc-indirect-tax-news-roundup-q3-2026.pdf
- https://www.wafeq.com/en-kw/tax-and-reporting/accounting-requirements-for-companies-in-kuwait
- https://kpmg.com/kw/en/insights/2026/04/kuwait-tax-alert-5-percent-tax-retention.html
- https://www.vatupdate.com/2026/07/24/kuwait-keeps-vat-off-the-table-no-adoption-in-the-2026-2030-fiscal-plan/ (headline seen in search; page did not load)

## Confidence notes
- No Ministry of Finance page was read directly.
- 10-year retention reported by Wafeq without citing the statute.
- 5% retention: KPMG describes it for government bodies; Wafeq says companies in general. Confirm scope.
- "VAT not in 2026-2030 plan" is from a headline only.
- Commercial invoice fields are good practice, not taken from Kuwaiti law.
