# United Kingdom (GB) - invoice & bookkeeping profile

> Last checked: 2026-11-13. Not tax advice: confirm with an accountant or HMRC.

## At a glance
| Item | Value |
|---|---|
| Tax name | VAT |
| Tax authority | HM Revenue & Customs (https://www.gov.uk/government/organisations/hm-revenue-customs) |
| Rates | 20% standard; 5% reduced; 0% zero-rated; exempt |
| Registration threshold | Check gov.uk for the current figure (it changes) |
| Currency | Invoices may be in another currency, but the VAT total must be shown in GBP |
| Tax ID | VAT number: `GB` + 9 digits (regex `^GB\d{9}$`; some formats have 12 digits or GD/HA prefixes) |
| Online tax-ID check | https://www.gov.uk/check-uk-vat-number |
| Filing | Usually quarterly via Making Tax Digital (MTD) software |
| Record retention | At least 6 years (10 years for OSS/MOSS records) |

## Full VAT invoice: required fields (VAT Notice 700, section 16)
1. Unique sequential number
2. Issue date, and time of supply (tax point) if different
3. Supplier's name, address and VAT number
4. Customer's name and address
5. Description of goods or services
6. For each line: quantity, unit price excluding VAT, VAT rate
7. Any discounts
8. Total excluding VAT, total VAT

## Simplified invoice
For sales up to GBP 250 (including VAT): supplier's name, address and VAT number, tax point, description, and for each rate the total including VAT and the rate.

## Making Tax Digital
VAT records must be kept digitally in MTD-compatible software. When several programs are used, they must be digitally linked (no copy-paste between them). This skill's registers are working papers for the accountant, not MTD software.

## E-invoicing
All businesses must be able to send and receive VAT invoices electronically from **April 2029**, via Peppol (HMRC policy paper, 28 Oct 2026). Detailed rules are to follow.

## Checks the skill must run
- Full invoice fields present; simplified only up to GBP 250.
- VAT number format and the gov.uk check suggested for new suppliers.
- Foreign-currency invoices show the VAT in GBP.
- Rates are 20/5/0 or exempt.

## Sources
- https://www.gov.uk/guidance/vat-guide-notice-700
- https://www.gov.uk/guidance/record-keeping-for-vat-notice-70021
- https://www.gov.uk/charge-reclaim-record-vat/keeping-vat-records
- https://www.gov.uk/government/publications/vat-electronic-invoicing/e-invoicing-requirements

## Confidence notes
- Some of the full-invoice field list is from general knowledge of Notice 700. Verify it against section 16.
- The registration threshold is deliberately not stated. Check gov.uk.
