# Bahrain (BH) - invoice & bookkeeping profile

> Last checked: 2026-11-13. Rules change often. Not tax advice: confirm anything important with a Bahrain tax adviser or the National Bureau for Revenue (NBR).

## At a glance
| Item | Value |
|---|---|
| Tax name | VAT (Decree-Law No. 48 of 2018) |
| Tax authority | National Bureau for Revenue (NBR), https://www.nbr.gov.bh |
| Rates | 10% standard; 0% zero-rated (e.g. exports, basic food items, healthcare, education - check list); exempt (e.g. some financial services, bare land/residential property) |
| Registration threshold | Mandatory above BHD 37,500 annual taxable supplies (actual or expected next 12 months); voluntary above BHD 18,750; non-residents: no threshold |
| Currency | BHD (3 decimals: 1 BHD = 1,000 fils). Foreign currency allowed, but values and VAT must be shown in BHD with the Central Bank of Bahrain rate on the supply date |
| Tax ID name & format | VAT account number: 15 digits, numbers only, no "BH" prefix. Regex `^\d{15}$` (format only; no published check digit) |
| Online tax-ID check | NBR VAT payer lookup (by VAT number or CR number): https://www.nbr.gov.bh/vat/tp/ms |
| Filing frequency & deadline | Monthly if annual supplies > BHD 3m; otherwise generally quarterly. Return and payment due by the last day of the following month |
| Record retention | 10 years (extended from 5 years in 2024); 15 years for real estate records |

## Full tax invoice: required fields
1. "Tax Invoice" clearly shown
2. Supplier name, address and VAT account number
3. Customer name and address (and customer VAT number for B2B - see confidence notes) - **often missed**
4. Date of issue; date of supply or payment if different
5. Sequential invoice number
6. Description and quantity, enough to decide the VAT treatment
7. Unit price excl. VAT in BHD
8. Value before discount, discount, value after discount (excl. VAT, BHD)
9. VAT rate and VAT amount in BHD
10. Total incl. VAT in BHD
11. Exchange rate (CBB) if a foreign currency is used - **often missed**
12. Reference to profit margin scheme, or to the exemption/zero-rating, where it applies
- Issue by the 15th day of the month after the month of supply.
- Real estate (from Aug 2026): a VAT invoice is needed for all supplies, with a detailed description; new-build invoices must show the building permit number.

## Simplified invoice / receipt
- Allowed when the recipient is not VAT-registered, or when the consideration does not exceed BHD 500 (see confidence notes).
- Minimum fields: supplier name, address, VAT number; issue date; description; VAT rate and amount in BHD; total incl. VAT in BHD.
- For input VAT on a business purchase over BHD 500, expect a full tax invoice.

## Credit and debit notes
- Labelled "Credit Note" or "Debit Note"; supplier and customer details, supplier VAT number, sequential note number, issue date, **original invoice number**, adjustment value and VAT in BHD.
- Issue in the tax period when the adjusting event happens.

## E-invoicing / clearance status (as of 2026-11-13)
- **No mandatory e-invoicing or clearance.** Post-audit VAT system: invoices go directly supplier to customer.
- NBR tendered for a central e-invoicing platform in 2023; PwC (Q3 2026) reports a pilot phase launched, with **no implementation date announced**.
- Since 16 Nov 2023, VAT-registered persons may issue and keep electronic invoices (e.g. PDF) without prior NBR approval.
- **The skill must NOT fake** any clearance number, QR code or "NBR validated" mark. If NBR announces a mandate, re-check this file before issuing invoices.

## Numbering & language
- Sequential numbering; separate series allowed if each is sequential and unique.
- Arabic or English accepted.

## Reverse charge, imports & cross-border
- Services from non-resident suppliers to a Bahrain VAT-registered business: the customer usually self-accounts (reverse charge). Domestic reverse charge may also apply in some sectors.
- Imports of goods: VAT paid/deferred at customs; keep the customs declaration.
- GCC supplier invoices: VAT treatment depends on GCC rules; `ASK ACCOUNTANT`.

## Checks the skill must run for this country
- Document titled "Tax Invoice" (or "Simplified Tax Invoice" / "Credit Note" / "Debit Note").
- Supplier VAT account number present and matches `^\d{15}$`; new suppliers: remind user to check it on the NBR lookup and keep a dated screenshot.
- VAT rate is 10% or 0%; VAT = net x 10% (round to 0.001 BHD per line, i.e. fils, and say so).
- Amounts in BHD use 3 decimals; a 2-decimal BHD total is not an error but note it.
- Foreign-currency invoice: BHD value, BHD VAT and exchange rate shown.
- Simplified invoice above BHD 500 used for a VAT claim: flag.
- Exempt or zero-rated line: invoice cites the reason/reference; otherwise `CHECK`.
- Real estate invoice for a new build: building permit number present.
- Foreign supplier, no VAT: flag reverse charge; `ASK ACCOUNTANT` if unsure.

## Common mistakes
- VAT shown only in USD/SAR, not in BHD.
- Using 2 decimals and losing fils in VAT totals.
- Missing original invoice number on credit notes.
- Keeping records for only 5 years (now 10).

## Sources
- https://www.flick.network/en-bh/e-invoicing-bahrain
- https://ey.com/en_gl/tax-alerts/bahrain-issues-vat-invoicing-requirements
- https://www.avalara.com/us/en/vatlive/country-guides/africa-and-middle-east/bahrain/bahraini-vat-registration.html
- https://lookuptax.com/docs/tax-identification-number/bahrain-tax-id-guide
- https://www.vatupdate.com/2024/04/12/bahrain-extends-vat-record-retention-period-to-10-years
- https://www.pwc.com/m1/en/tax/documents/2026/gcc-indirect-tax-news-roundup-q3-2026.pdf

## Confidence notes
- No NBR page was read directly; the lookup URL is as reported by LookupTax.
- BHD 500 simplified-invoice threshold from a vendor guide (Flick); EY's summary did not show the conditions. Verify with NBR.
- Whether the customer's VAT number is mandatory on a full tax invoice was not confirmed (EY lists name and address only). Ask the accountant; the skill should still flag it as recommended for B2B.
- 10-year retention: effective date and legal basis not confirmed.
- Zero-rated/exempt examples are indicative, from general knowledge.
- Status of the e-invoicing pilot (who is in it, any planned dates) unclear.
