# Malaysia (MY) — invoice & bookkeeping profile

> Last checked: 2026-11-13. Rules change often. Not tax advice: confirm anything important with a local accountant or the tax authority.

## At a glance
| Item | Value |
|---|---|
| Tax name | Sales and Service Tax (SST) — two single-stage taxes, **not a VAT** (no general input-tax credit) |
| Tax authority | SST: Royal Malaysian Customs Department (JKDM) — https://sst.customs.gov.my ; Income tax & e-Invoice: Inland Revenue Board (LHDN / HASiL) — https://www.hasil.gov.my |
| Rates | **Sales tax** (manufacturers/importers of goods): 5% or 10%; some essentials 0%/exempt. **Service tax** (prescribed services): generally 8%; 6% for F&B, telecoms, parking, logistics, construction, education & healthcare for non-citizens, rental/leasing (6% from 1 Jan 2026); flat RM25 for charge/credit cards |
| Registration threshold | Sales tax: RM500,000 taxable sales/12 months (manufacturers). Service tax: RM500,000 generally; F&B RM1.5m; construction RM1.5m; rental/leasing RM1m; some services nil |
| Currency | MYR (RM). Foreign-currency invoices common; tax amounts should be reported in RM |
| Tax ID name & format | Income-tax **TIN** (needed on e-Invoices): individuals `IG` + 9–11 digits (older `OG`/`SG`); companies `C` + 10–11 digits ending in an added `0` (e.g. `C20830570210`); other entities 1–2 letter prefix. **SST registration no.** is separate (e.g. `W10-1808-32000001`) |
| Online tax-ID check | MyInvois portal / API TIN validation (LHDN); MySST portal for SST registration status |
| Filing frequency & deadline | SST-02 return every 2 months; file & pay by the last day of the month after the taxable period |
| Record retention | 7 years (SST and income tax) |

## Full tax invoice: required fields
For SST-registered sellers (sales tax or service tax invoice):
1. Invoice serial number (sequential, no gaps/duplicates)
2. Invoice date
3. Seller's name, address and **SST registration number** (*only SST-registered persons may charge SST*)
4. Buyer's name and address (and SST reg no. if registered)
5. Description of goods/services
6. Quantity and unit price
7. Total **excluding** tax
8. **Tax rate** (5%/10% sales tax or 6%/8% service tax) and **tax amount shown separately** (*often missed*: mixing 6% and 8% services on one invoice without line-level rates)
9. Total payable

If in e-Invoice scope, the invoice must additionally be a **validated MyInvois e-Invoice** (see below), which adds supplier & buyer TIN, ID/registration number, MSIC code, classification codes, and the LHDN validation UUID + QR code.

## Simplified invoice / receipt
SST has no "simplified tax invoice" concept like VAT countries. Retail receipts from SST-registered sellers should still show seller name, SST no., date, items, tax amount. Under e-Invoicing, B2C sales where the buyer does not request an e-Invoice may be covered by a **consolidated e-Invoice** submitted monthly (within 7 days after month-end) — but **any single transaction above RM10,000** needs its own e-Invoice (from 1 Jan 2026). Buyers cannot reclaim SST (not a VAT); for income-tax deductibility, in-scope buyers need a validated e-Invoice.

## Credit and debit notes
Must reference the original invoice number and date, state the reason and adjusted tax. For e-Invoice taxpayers: a validated e-Invoice can be **cancelled within 72 hours**; after that, corrections are made by **credit note / debit note / refund note e-Invoices** referencing the original e-Invoice UUID.

## E-invoicing / clearance status (as of last-checked date)
- **System**: MyInvois (LHDN). **Clearance-style**: invoice data is submitted to MyInvois, validated in near real time, and LHDN returns a **unique identifier (UUID)** and a validation link/QR code that must appear on the e-Invoice shared with the buyer.
- **Phases** (annual turnover): >RM100m from 1 Aug 2024; RM25–100m from 1 Jan 2025; RM5–25m from 1 Jul 2025; Phase 4 from 1 Jan 2026 (originally RM1–5m).
- **Small-business exemption**: businesses below RM1m were exempted (announced Dec 2025); **from 1 Sep 2026 the exemption threshold was raised to RM3 million** annual sales. Businesses below RM3m are not required to e-Invoice (voluntary participation encouraged) and may issue non-electronic invoices. The planned RM500k–1m phase is no longer applicable.
- Reported (non-official source): relaxation period for Phase 4 taxpayers to 31 Dec 2027 (consolidated monthly e-Invoices allowed, no penalties if conditions met; RM10,000 rule still applies).
- General TINs when buyer/supplier TIN is unknown: `EI00000000010` (Malaysian individual, only MyKad given), `EI00000000020` (foreign buyer), `EI00000000030` (foreign supplier).
- **The skill must NOT** fabricate MyInvois UUIDs, validation links, QR codes or "validated" status. In-scope users must issue via the MyInvois Portal/API or their certified software; the skill may only draft data and check fields.

## Numbering & language
- Sequential numbering; separate series per branch/type acceptable if unique.
- Bahasa Malaysia or English.

## Reverse charge, imports & cross-border
- Imported taxable services acquired by a business: service tax at 8% self-accounted by the recipient (reverse-charge style) — declare via SST-02A if not SST-registered.
- Foreign digital service providers register for service tax (threshold RM500,000) and charge 8% to Malaysian consumers.
- Imported goods: sales tax collected by Customs at import.
- e-Invoice: purchases from foreign suppliers by in-scope businesses require a **self-billed e-Invoice** (using `EI00000000030` if no supplier TIN).

## Checks the skill must run for this country
- If a supplier charges SST, the invoice shows an SST registration number (format `^[A-Z]\d{2}-\d{4}-\d{8}$` as a loose check); if missing, flag "SST charged without SST no.".
- Service tax rate is 6% or 8% consistent with the service type (e.g. F&B/logistics/construction 6%; professional/IT/management 8%; rental 6% from 1 Jan 2026); sales tax 5% or 10%. Flag any other rate (e.g. 10% service tax).
- Tax is not treated as recoverable input tax in the books (SST is a cost) unless the user's accountant confirms a specific credit.
- TIN format: individual `^IG\d{9,11}$`; non-individual `^[A-Z]{1,2}\d{9,12}$`; or one of the general EI TINs. Never mark as "valid" without MyInvois validation by the user.
- Ask annual turnover: if ≥ RM3m (and in phase), every sales invoice must be a validated e-Invoice with UUID + QR; flag paper/PDF-only invoices.
- For in-scope users: any B2C transaction > RM10,000 must have an individual e-Invoice (not consolidated).
- Purchase invoices from in-scope suppliers should carry a UUID/QR; if absent, ask the supplier for the validated e-Invoice.
- Credit/debit notes reference the original invoice no. (and UUID if e-Invoice).
- Maths: Σ lines excl. tax × rate = tax amount (±RM0.01 rounding).

## Common mistakes
- Treating SST like VAT and claiming it back.
- Applying the old 6% service tax across all services after the 2024/2025 changes.
- Non-SST-registered suppliers adding "SST" to invoices.
- Using a company registration number (SSM) in place of the LHDN TIN on e-Invoices.
- Consolidating a large (>RM10,000) B2C sale.

## Sources
- https://thestar.com.my/news/nation/2026/08/30/over-11-million-businesses-to-benefit-from-higher-e-invoicing-threshold-says-lhdn
- https://kpmg.com/us/en/taxnewsflash/news/2026/09/malaysia-e-invoicing-threshold-increased-rm3-million-effective-september-1-2026.html
- https://www.malaymail.com/news/malaysia/2026/08/31/irb-stresses-voluntary-participation-as-government-lifts-einvoice-threshold-easing-compliance-for-msmes/233340
- https://beancount.io/blog/2026/09/16/malaysia-e-invoicing-phase-4-rm3m-exemption-rm10000-rule-guide (non-official)
- https://kpmg.com/my/en/home/insights/2025/06/review-of-goods-for-sales-tax-and-expansion-of-scope-for-service-tax.html
- https://www.pwc.com/my/en/publications/mtb/service-tax.html
- https://www.airwallex.com/en-my/blog/sst-invoice-format-malaysia
- https://www.cleartax.com/my/en/tin-malaysia

## Confidence notes
- Official LHDN e-Invoice pages (hasil.gov.my) could not be fetched this session; e-Invoice details come from news (The Star, Malay Mail, KPMG) and secondary guides.
- RM3m threshold from 1 Sep 2026: confirmed by multiple news sources. Relaxation to 31 Dec 2027, the 7-day consolidated deadline and penalty figures come from a non-official blog — verify on hasil.gov.my.
- Unclear how businesses between RM1m and RM3m that already started e-Invoicing are treated (may continue voluntarily).
- Service tax rental/leasing 6% from 1 Jan 2026 and thresholds from PwC Tax Booklet; Budget 2027 changes (e.g. elderly care to 6%) only proposed.
- SST registration number format, 7-year retention, sales-tax RM500k threshold and SST-02A mechanism not re-verified this session.
- TIN length descriptions vary between sources (11–13 characters).
