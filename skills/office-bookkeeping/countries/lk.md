# Sri Lanka (LK) — invoice & bookkeeping profile

> Last checked: 2026-11-13. Rules change often. Not tax advice: confirm anything important with a local accountant or the Inland Revenue Department.

## At a glance
| Item | Value |
|---|---|
| Tax name | Value Added Tax (VAT), VAT Act No. 14 of 2002 (as amended, incl. Amendment Act No. 14 of 2026). Also the **Social Security Contribution Levy (SSCL)**, a separate turnover levy |
| Tax authority | Inland Revenue Department (IRD), ird.gov.lk. Online system: RAMIS / IRD e-Services |
| Rates | **18%** standard (since 1 Jan 2024). **Financial services 20.5%** for periods from 1 Jul 2026. 0% for exports of goods and specified services. Exempt supplies listed in the Act. SSCL: **2.5%** on liable turnover (see Confidence notes) |
| Registration threshold | Taxable supplies > **LKR 15 million in a quarter** or > **LKR 60 million in 12 months** (or expected to). Apply within 15 days. A proposed cut to LKR 36 million (for VAT and SSCL) was **abandoned** in June 2026. Importers/exporters of goods for business must register. Non-resident digital service providers: same thresholds, from 1 Jul 2026 |
| Currency | LKR. Invoice amounts in LKR to 2 decimals |
| Tax ID name & format | **TIN**: 9 digits (`^\d{9}$`). VAT registration is a tax type under the TIN. VAT numbers are commonly written as TIN + `-7000` (see Confidence notes) |
| Online tax-ID check | IRD e-Services (RAMIS) taxpayer/VAT registration search (on ird.gov.lk) |
| Filing frequency & deadline | VAT return by the **last day of the month after** each taxable period (monthly for most registrants; quarterly for some). E-filing mandatory from 1 Jul 2025. VAT schedules are uploaded to RAMIS (CSV, portal or Web API) |
| Record retention | Keep the duplicate of each tax invoice **5 years** after the end of the taxable period (s.20). Same period for other records |

## Full tax invoice: required fields
New mandatory tax invoice format (IRD circular SEC/2026/E/03; in force by Oct 2026, see Confidence notes):
1. Heading **"TAX INVOICE"**, shown prominently.
2. Supplier's **9-digit TIN**, registered name and address (exactly as on the VAT certificate).
3. Purchaser's TIN, name and address if the purchaser is VAT-registered.
4. **Invoice date and date of supply**, shown separately (often missed).
5. Serial number in the form **`YYMMM_QQQQ_XXXXX`** (e.g. `26OCT_COLBR_00125`): 2-digit year, 3-letter month, a 1–15 char classification code (branch/department/type), and a sequential number. **Max 40 characters, no spaces**, unbroken sequence. ERP-RAMIS API integrators approved before 1 Jul 2026 may omit the prefix if integrated by 31 Dec 2026.
6. Description and quantity of goods/services.
7. Three-line breakdown: **value excluding VAT, VAT amount, total including VAT** (LKR, 2 decimals).
- Optional: payment mode, place of supply, amount in words, notes. Logos and extra columns are allowed.
- Must be issued **within 28 days** of supply when a registered buyer asks for one (written request within 14 days, or the buyer states they're registered).

## Simplified invoice / receipt
- For unregistered buyers: issue an invoice showing the total consideration **including VAT**. This is **not** a tax invoice and can't support an input-tax claim.
- IRD announced that registered persons must use **secured POS machines** within 3 months of a date still to be prescribed (specifications pending).

## Credit and debit notes
- s.25: issued when the tax on a tax invoice was over- or under-charged (incl. returns or price changes). They must be in the specified form and reference the original tax invoice.
- **Time limit: not later than 6 months after the original tax invoice was issued** (where input tax was claimed on it).
- The supplier adjusts output tax and the registered buyer adjusts input tax in the same direction.

## E-invoicing / clearance status (as of last-checked date)
- **National e-Invoicing System** (announced May 2026): real-time transmission from ERP to RAMIS via Web API. Pilot with tea brokers from 1 May 2026. Phase 1: export-oriented VAT payers (tea, garments). Phase 2: **all VAT-registered persons targeted by end-2026**. **Not yet a universal mandate.**
- The new tax invoice format applies to everyone now, whether or not they are on e-invoicing.
- SVAT (Simplified VAT for exporters) was **abolished 1 Oct 2025** and replaced by a Risk-Based Refund Scheme (refund generally within 45 days). Don't accept new "SVAT credit voucher" invoices.
- **The skill must NEVER invent a TIN, RAMIS acknowledgement, e-invoice reference or POS fiscal number.** Drafts are marked "DRAFT".

## Numbering & language
- Serial structure as above (max 40 chars, no spaces, continuous). One sequence per classification code.
- English is normal for invoices. Sinhala/Tamil are also official languages.

## Reverse charge, imports & cross-border
- Imports of goods: VAT collected by Customs on the CusDec. Input claims on a CusDec must be made within 24 months.
- From 1 Jul 2026, **non-resident e-platform/digital services** to Sri Lankan customers attract 18% VAT. The non-resident registers above the threshold. For **B2B supplies to VAT-registered recipients no VAT is charged**: the non-resident files a simplified statement instead.
- Exports: zero-rated. Keep export evidence. Refunds go through the Risk-Based Refund Scheme.

## Checks the skill must run for this country
- Supplier TIN matches `^\d{9}$` (a `-7000` VAT suffix is tolerated). Purchaser TIN is present if the buyer is VAT-registered (required for the buyer's input claim).
- Heading "TAX INVOICE" present.
- Both invoice date and supply date present. Invoice date − supply date ≤ 28 days.
- Serial number ≤ 40 chars, no spaces. For invoices dated ≥ Oct 2026 it matches `^\d{2}(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)_[A-Z0-9]{1,15}_\d+$` (flag, not reject, if missing: API-integrator relaxation until 31 Dec 2026). YY/MMM matches the invoice date.
- VAT rate 18% (20.5% only for financial services from 1 Jul 2026; 0% only with export evidence).
- Arithmetic: value excl. VAT × rate = VAT (±0.01 LKR per line, ±1 total); excl. + VAT = total; amounts in LKR with 2 decimals.
- Input-tax claim window: the tax invoice was received within 12 months of the end of the taxable period and is claimed within **12 months of the invoice date**. Flag older invoices.
- Credit/debit note references the original invoice and is dated ≤ 6 months after it.
- SSCL is not shown as VAT. If the supplier passes on SSCL, it's a separate cost line (VAT treatment: see Confidence notes).

## Common mistakes
- Using the old invoice layout (missing supply date, wrong serial format, or no TIN on the buyer side).
- Claiming input tax on "invoices" issued to unregistered persons, or on invoices older than 12 months.
- Still treating supplies as SVAT after 1 Oct 2025.
- Assuming the LKR 36 million threshold applies: it was dropped.

## Sources
- https://www.taxadvisor.lk/data/uploads/consolidated_text_of_the_value_added_tax_act_no_14_of_2002_incorporating_amendments_up_to_31_12_2025_.pdf (consolidated VAT Act: ss.10, 20, 21, 22, 25)
- https://www.taxadvisor.lk/data/uploads/notice_to_taxpayers_13_07_2026_.pdf (IRD notice on the 2026 Amendment Act)
- https://lookuptax.com/docs/country/sri-lanka-vat-guidelines-indirect-tax
- https://lookuptax.com/tax-changes/sri-lanka/vat-invoice-format-2026
- https://beancount.io/blog/2026/09/24/sri-lanka-vat-threshold-reversal-60-million-registration-guide
- https://www.ft.lk/front-page/Sri-Lanka-ends-SVAT-starts-risk-based-VAT-refund-scheme-today/44-782409
- https://www.taxadvisor.lk/article/tc1 (SSCL threshold timeline; its July 2026 reduction appears superseded)

## Confidence notes
- **Invoice format start date conflicts:** one source says fully in force 1 Jul 2026 (Circular SEC/2026/E/03). Another says it was postponed to 1 Oct 2026 by Gazette 2500/106. Either way it's in force by the check date. ird.gov.lk was not fetched in this session.
- **SSCL:** the 2.5% rate and liable-turnover basis are well known but not verified here. The current SSCL threshold is believed to be LKR 60m/year (15m/quarter), since the 36m cut was dropped for both VAT and SSCL (news headline). One adviser page still lists 36m from Jul 2026. VAT treatment of SSCL passed on to customers is not verified.
- The VAT number "TIN-7000" convention, taxable period lengths (monthly vs quarterly) and the general record-keeping period under s.64 were not verified.
- The e-invoicing phase dates are announcements, not legislation.
