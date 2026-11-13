# Philippines (PH) — invoice & bookkeeping profile

> Last checked: 2026-11-13. Rules change often. Not tax advice: confirm anything important with a local accountant or the tax authority.

## At a glance
| Item | Value |
|---|---|
| Tax name | Value-Added Tax (VAT); non-VAT businesses pay Percentage Tax |
| Tax authority | Bureau of Internal Revenue (BIR) — https://www.bir.gov.ph |
| Rates | 12% standard; 0% zero-rated (exports, qualifying services to foreign clients); VAT-exempt sales |
| Registration threshold | VAT registration required when gross sales/receipts exceed PHP 3,000,000 in any 12-month period |
| Currency | PHP. Foreign-currency invoices should also show PHP equivalent for VAT |
| Tax ID name & format | TIN: 9 digits + branch code (`000` / `00000` for head office), printed e.g. `123-456-789-00000`. Regex: `^\d{3}-?\d{3}-?\d{3}(-?\d{3,5})?$` |
| Online tax-ID check | No public BIR TIN lookup; verify via the supplier's BIR Certificate of Registration (Form 2303) |
| Filing frequency & deadline | Quarterly VAT return (BIR Form 2550Q), due the 25th day after quarter end |
| Record retention | At least 5 years |

## Full tax invoice: required fields
Since the **Ease of Paying Taxes (EOPT) Act** and **RR 7-2024** (as amended by RR 11-2024), the **invoice is the only primary document** for both goods and services. **Official Receipts (ORs) no longer support input VAT.**
1. Document title **"Invoice"** in prominent place (may be "Sales Invoice", "Service Invoice", "Cash/Charge/Billing Invoice")
2. Seller's registered name (as on COR), **"VAT REG TIN"** + branch code, registered business address
3. Serial number (BIR-registered series) and transaction date
4. Buyer's registered name (or customer name for B2C), **buyer TIN**, address — *often missed* on B2B invoices
5. Description of goods / nature of service, quantity, unit price, amount
6. Total sale incl. VAT, discounts, exemptions
7. **VAT amount shown separately** + breakdown of **VATable / zero-rated / VAT-exempt** sales where applicable
8. Printer / system authority details: ATP or acknowledgment/permit no. (CAS/POS), date issued, approved serial range

Minimum for buyer's input VAT if other items are missing: sales amount, VAT amount, registered names and TINs of buyer and seller, description, transaction date.

## Simplified invoice / receipt
- A VAT-registered seller should issue a VAT invoice **for every sale regardless of amount**.
- ORs, collection receipts, acknowledgment receipts and payment receipts are now **supplementary documents** (proof of payment only). Old ORs had to be stamped "THIS DOCUMENT IS NOT VALID FOR CLAIM OF INPUT TAX"; conversion of unused ORs into invoices was allowed only until 31 Dec 2024.
- **ORs dated after 31 Dec 2024 cannot support input VAT**.

## Credit and debit notes
Must reference the original invoice number/date, show the adjusted VAT and the reason (returns, discounts). Keep with original invoice. (No specific time limit verified.)

## E-invoicing / clearance status (as of last-checked date)
- **System**: BIR Electronic Invoicing System (EIS) — sellers transmit e-invoice/sales data to BIR.
- **Mandate**: RMC 98-2026 (22 Sep 2026), implementing RR 8-2022 and RR 11-2025 as amended by RR 26-2025, requires covered taxpayers to **shift to e-invoices by 31 Dec 2026**. Covered: taxpayers in e-commerce/online sales, Large Taxpayers, and businesses using Computerized Accounting Systems (CAS) / computerized books / invoicing software. **Micro taxpayers excluded.** Separate e-sales-reporting rules to follow.
- Can use in-house system, commercial software or an accredited e-invoicing service provider.
- **The skill must NOT** fabricate BIR acknowledgment/transmission IDs, ATP/PTU numbers or claim an invoice was transmitted to EIS. Covered users must issue through their registered CAS/EIS-certified system.

## Numbering & language
- Serial numbers must follow the BIR-registered/ATP-approved series; systems that converted from ORs continue the last approved serial.
- English or Filipino.

## Reverse charge, imports & cross-border
- Services from non-resident suppliers consumed in the Philippines: buyer withholds/remits **12% final VAT** (BIR Form 1600-VT) and may claim it as input VAT.
- Import VAT collected by Bureau of Customs.
- Zero-rated sales (exports, services paid in acceptable foreign currency to non-residents): invoice must state "zero-rated sale".

## Checks the skill must run for this country
- Document titled "Invoice"; reject "Official Receipt" for input-VAT claims (flag if dated after 31 Dec 2024).
- Seller TIN matches regex and is prefixed "VAT REG TIN" when VAT is charged; non-VAT seller charging VAT → flag.
- B2B: buyer's registered name and TIN present on purchase invoice.
- VAT = 12% × VATable sales (or VAT = total × 12/112 for VAT-inclusive pricing); tolerance ±PHP 0.01.
- Breakdown of VATable / zero-rated / exempt totals present when mixed.
- ATP/permit details and serial number present.
- Ask if user is covered by e-invoicing (online sales, Large Taxpayer, CAS user, not micro); if covered, from 31 Dec 2026 sales invoices must be issued via their EIS-compliant system.
- Foreign services purchased: remind about final VAT withholding (1600-VT).

## Common mistakes
- Still issuing/accepting Official Receipts for services.
- Missing buyer TIN on B2B invoices.
- VAT computed on gross instead of 12/112 for inclusive prices.
- Unregistered invoice series (no ATP).

## Sources
- https://forvismazars.com/ph/en/insights/tax-alerts/ease-of-paying-taxes-act/vat-invoicing-requirements-eopt-act
- https://www.pwc.com/ph/en/tax/tax-publications/taxwise-or-otherwise/2024/compliance-change-on-invoicing-under-eopt.html
- https://www.grantthornton.com.ph/insights/articles-and-updates1/tax-notes/clarification-on-the-invoicing-requirements-per-rr-no-7-2024-as-amended-by-rr-no-11-2024/
- https://invoicedataextraction.com/blog/philippines-invoice-requirements-after-eopt
- https://tribune.net.ph/2026/09/23/bir-sets-31-december-e-invoicing-deadline
- https://stripe.com/en-br/resources/more/philippines-vat-rate-registration-rules-and-compliance-basics

## Confidence notes
- bir.gov.ph pages were not fetched; invoice particulars come from secondary summaries of RR 7-2024 / RMC 77-2024.
- E-invoicing mandate details from one news article (Daily Tribune); confirm RMC 98-2026 scope and whether exporters are separately covered.
- Branch code length (3 vs 5 digits), buyer-detail threshold for B2C sales (sometimes cited as PHP 1,000), final VAT form number, and credit-note rules not verified.
- PHP 3m threshold, quarterly 2550Q and 5-year retention from a secondary source (Stripe), consistent with known rules.
