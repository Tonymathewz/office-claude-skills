# United States (US) — invoice & bookkeeping profile

> Last checked: 2026-11-13. Rules change often. Not tax advice: confirm anything important with a local accountant or the tax authority. Sales tax is state/local — this file is deliberately general.

## At a glance
| Item | Value |
|---|---|
| Tax name | **No federal VAT/GST.** State and local sales & use tax; federal income tax and information reporting (Forms 1099) |
| Tax authority | Federal: Internal Revenue Service (IRS) — https://www.irs.gov. Sales tax: each state's revenue department |
| Rates | Set by state + county/city/district; vary by product. No statewide sales tax in Alaska, Delaware, Montana, New Hampshire, Oregon (Alaska has local sales taxes) |
| Registration threshold | Sales-tax registration where you have nexus. Since *South Dakota v. Wayfair* (2018) every sales-tax state has economic nexus, typically $100,000 of sales (some states $250k/$500k, some still with a transaction count) |
| Currency | USD in practice; no federal invoice-currency rule |
| Tax ID name & format | EIN `^\d{2}-?\d{7}$` (XX-XXXXXXX); SSN/ITIN `^\d{3}-?\d{2}-?\d{4}$` for individuals. State sales-tax permit numbers vary by state |
| Online tax-ID check | IRS TIN Matching (e-Services, for 1099 payers) — see Confidence notes |
| Filing frequency & deadline | Sales tax: monthly/quarterly/annual per state. 1099-NEC to IRS and recipient by 31 January following year (see Confidence notes) |
| Record retention | IRS: generally 3 years after filing; 6 years if income under-reported >25%; 7 years for bad-debt/worthless-securities claims; 4 years for employment tax; indefinitely if no return or fraud; property records until limitation period for year of disposal |

## Full tax invoice: required fields
No federal "tax invoice". Recommended minimum for sales invoices (and what to check on purchase invoices):
1. Seller legal name, address, (EIN optional)
2. Unique invoice number and date
3. Buyer name and address; **ship-to address** (drives sales-tax jurisdiction — often missed)
4. Description, quantity, unit price
5. Subtotal, **sales tax shown separately** with jurisdiction/rate, total
6. If no tax charged: reason (resale/exempt certificate on file, out-of-state, non-taxable item)
7. Payment terms

### 1099 vendor process (W-9)
- Collect **Form W-9** (name, TIN, entity type) from each US vendor *before first payment*.
- Forms 1099-NEC / 1099-MISC: threshold raised from $600 to **$2,000 for payments made after 31 Dec 2025** (i.e. 2026 payments, filed early 2027); inflation-indexed from 2027.
- 1099-K threshold back to >$20,000 and >200 transactions.
- Payments by card/PayPal-type networks are reported by the processor on 1099-K, not by you on 1099-NEC (see Confidence notes).
- Missing/incorrect TIN can require backup withholding.

### Resale & exemption certificates
- A buyer claiming resale/exemption must give the seller a certificate (state form or the MTC Uniform Sales & Use Tax Certificate, latest version 14 Oct 2022; acceptance varies by state).
- Seller must accept in good faith and keep it on file; some states require renewal. No certificate → charge tax.

## Simplified invoice / receipt
- No regime. A receipt showing payee, date, amount and what was bought is the usual expense support. Keep card/bank statements as backup, not replacement.

## Credit and debit notes
- No federal format. Good practice: own number, date, original invoice reference, reason, amount, and reversed sales tax (if tax was charged, refund it to the customer or the state per state rules).

## E-invoicing / clearance status (as of last-checked date)
- **No federal or state B2B e-invoicing mandate.** Voluntary networks exist.
- The skill must not fabricate EINs, TINs, state permit numbers or exemption certificate numbers.

## Numbering & language
- No legal rule; unique sequential numbers recommended. English.

## Reverse charge, imports & cross-border
- No reverse charge. If a seller didn't charge sales tax on a taxable item used in a state where you are registered, the buyer usually owes **use tax** to that state — flag to accountant.
- Imports: customs duties are separate from sales tax.

## Checks the skill must run for this country
- Every US vendor paid in the year has a W-9 on file before payment; TIN matches EIN or SSN format.
- Year-to-date payments per non-corporate vendor ≥ $2,000 (for 2026 payments) → flag "1099-NEC likely"; exclude card/processor payments.
- Sales invoice: tax line present unless a valid, unexpired exemption/resale certificate is on file for that customer and state.
- Exemption certificate fields complete: buyer name, address, state ID per state, reason, signature, date.
- Ship-to state is a state where we're registered → tax charged; NOMAD states → no state sales tax (Alaska: check local).
- Purchase invoice with no sales tax on a taxable item → flag possible use tax.
- Retention: never purge records younger than 3 years after the related return filing; employment records 4 years.

## Common mistakes
- Paying contractors without collecting W-9 first.
- Using the old $600 1099 threshold for 2026 payments (or the new $2,000 for 2025 payments).
- Accepting an incomplete/expired resale certificate.
- Charging tax based on billing address instead of ship-to.

## Sources
- https://irs.gov/businesses/small-businesses-self-employed/how-long-should-i-keep-records (IRS record retention)
- https://sovos.com/regulatory-updates/trr/one-big-beautiful-bill-raises-1099-reporting-thresholds/ ($2,000 1099-NEC/MISC from payments after 31 Dec 2025; 1099-K $20k/200)
- https://mtc.gov/resources/faq-uniform-sales-and-use-tax-certificate/ (Uniform multijurisdictional certificate, good faith)
- https://www.avalara.com/us/en/blog/states-with-no-sales-tax-what-you-need-to-know.html (NOMAD states, Wayfair, nexus threshold types)

## Confidence notes
- IRS TIN Matching program and 1099-NEC 31 January deadline are from general knowledge, not seen this session.
- "Corporations generally exempt from 1099-NEC (except e.g. attorneys)" and processor-payment exclusion are from general knowledge — confirm.
- Backup-withholding threshold interaction with the new $2,000 limit was not clearly confirmed.
- State nexus thresholds change frequently; check each state's revenue site.
