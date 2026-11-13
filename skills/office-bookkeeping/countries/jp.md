# Japan (JP) — invoice & bookkeeping profile

> Last checked: 2026-11-13. Rules change often. Not tax advice: confirm anything important with a local accountant or the tax authority.

## At a glance
| Item | Value |
|---|---|
| Tax name | Consumption Tax (消費税, JCT), incl. local consumption tax |
| Tax authority | National Tax Agency (国税庁, NTA) — https://www.nta.go.jp |
| Rates | Standard 10%; reduced 8% (food & non-alcoholic drink excl. dining out, certain newspaper subscriptions); 0% exports; some supplies non-taxable (e.g. land, residential rent, many financial services) |
| Registration threshold | Taxable sales over JPY 10 million in the base period (generally 2 years earlier) makes a business taxable. Registering as a Qualified Invoice Issuer is a separate, voluntary step, but buyers need it to claim full input tax |
| Currency | JPY normal; foreign currency invoices are used in practice — skill should still record JPY tax amounts for the books |
| Tax ID name & format | Qualified Invoice Issuer Registration Number (登録番号): `T` + 13 digits. Regex `^T\d{13}$`. Corporations: T + their 13-digit Corporate Number (法人番号); sole traders/foreign businesses get a separate 13-digit number |
| Online tax-ID check | Qualified Invoice Issuer Publication Site: https://www.invoice-kohyo.nta.go.jp (Corporate Numbers: https://www.houjin-bangou.nta.go.jp) |
| Filing frequency & deadline | Annual return (corporations: generally 2 months after year end; individuals: 31 March), plus interim returns depending on prior-year tax |
| Record retention | 7 years for books and invoices (see Confidence notes) |

## Full tax invoice: required fields
Qualified Invoice (適格請求書), per NTA:
1. Issuer's name and **registration number (T + 13 digits)** — most often missed / mistyped
2. Transaction date
3. Description of goods/services, **marking which items are reduced-rate (8%)** items (often missed)
4. Total consideration **per tax rate** (tax-excluded or tax-included) and the applicable rate
5. **Consumption tax amount per tax rate** (often missed: one total for mixed 10%/8% is not enough)
6. Name of the recipient (buyer)

Practice note: the tax per rate is normally rounded once per invoice per rate, not line by line.

### Supplier has no T-number: transitional input-tax credit
| Period | Creditable share of the "deemed" tax |
|---|---|
| 1 Oct 2023 – 30 Sep 2026 | 80% |
| **1 Oct 2026 – 30 Sep 2028** | **70% (current)** |
| 1 Oct 2028 – 30 Sep 2030 | 50% |
| 1 Oct 2030 – 30 Sep 2031 | 30% |
| From 1 Oct 2031 | 0% |
(FY2026 (令和8年度) reform; earlier schedule was 80% → 50% from Oct 2026 → 0% from Oct 2029.)
- Small registered sole traders: the "20% special rule" (2割特例) is available up to the 2026 return; a "30% rule" (3割特例) applies for 2027 and 2028 returns (individuals only).

## Simplified invoice / receipt
- Simplified Qualified Invoice (適格簡易請求書) allowed for businesses selling to many unspecified people: retail, restaurants, taxis, etc.
- Same as above except **buyer name may be omitted**, and it may show *either* the tax amount per rate *or* the rate (or both).
- Buyer can claim input tax on it.
- Small-amount relief: businesses with taxable sales ≤ JPY 100 million in the reference period may credit purchases under JPY 10,000 (tax-incl.) per transaction with only a ledger record, 1 Oct 2023 – 30 Sep 2029.

## Credit and debit notes
- Returns/discounts/rebates need a **Qualified Return Invoice** (適格返還インボイス): issuer name + registration number, date of the return/discount, date of the original sale, description, total refund per rate, and refund tax amount or rate.
- Returns under JPY 10,000 (tax-incl.) are exempt from issuing one (see Confidence notes).
- Errors in an issued invoice must be fixed by issuing a corrected qualified invoice to the buyer.

## E-invoicing / clearance status (as of last-checked date)
- **No clearance or government e-invoice mandate.** Paper, PDF, or structured e-invoices are all valid if they contain the required items.
- Peppol (JP PINT) exists but is voluntary.
- Data received electronically (PDF/email/portal) must be stored electronically under the Electronic Books Maintenance Act — printing and deleting is not enough.
- The skill must NOT invent a T-number or mark a supplier as registered without a lookup.

## Numbering & language
- No statutory sequential numbering rule, but a unique invoice number is standard practice and needed for audit trail.
- Japanese usual; other languages are not prohibited if required items are clear.

## Reverse charge, imports & cross-border
- B2B "electronically supplied services" from foreign suppliers are reverse-charged by the Japanese recipient (in practice only matters when the recipient's taxable sales ratio is below 95%). Foreign supplier should state that the Japanese customer accounts for the tax.
- Import JCT is paid to Customs; keep the import permit as the credit document, not a supplier invoice.

## Checks the skill must run for this country
- Supplier registration number present and matches `^T\d{13}$` (strip spaces/hyphens first).
- For corporate T-numbers: check digit of the 13-digit part = `9 - (Σ(P_n × Q_n) mod 9)`, where P_n is the n-th digit counting from the right of the last 12 digits and Q_n = 1 for odd n, 2 for even n. Fail → flag "possible typo" (warning only; confirm on invoice-kohyo).
- Prompt user to confirm T-number on the NTA publication site, and that the registered name matches the invoice.
- Invoice shows tax-inclusive or tax-exclusive totals **separately for 10% and 8%**, with each rate stated.
- Tax amount per rate ≈ base × rate (tolerance ±1 yen per rate for rounding).
- Reduced-rate items are marked (e.g. ※ or ★ with a legend).
- Full invoice shows buyer name (unless supplier is retail/restaurant/taxi type → simplified OK).
- No T-number → treat input tax as transitional: 70% of the tax for invoice dates 1 Oct 2026 – 30 Sep 2028 (use date-based table above), and flag the ledger note required.
- Credit note references original sale date and shows refund tax per rate.

## Common mistakes
- One combined tax figure for mixed 8%/10% items.
- Tax rounded per line instead of per rate per invoice.
- Treating an unregistered supplier's invoice as fully creditable.
- Supplier's registration lapsed or name differs from the publication site.
- Printing and deleting e-delivered invoices.

## Sources
- https://www.nta.go.jp/english/taxes/consumption_tax/pdf/2023/simplified_04.pdf (NTA: required items, simplified invoices, transitional %, small-amount relief)
- https://www.nta.go.jp/taxes/shiraberu/zeimokubetsu/shohi/keigenzeiritsu/pdf/0026004-066_01.pdf (NTA, Sept 2026: 70% from 1 Oct 2026, later steps, 2割/3割特例)
- https://www.ey.com/en_jp/technical/ey-japan-tax-library/tax-alerts/2025/tax-alerts-12-24 (FY2026 reform outline)
- https://support.yayoi-kk.co.jp/faq_Subcontents.html?page_id=31318 (70% / 3割特例 summary)
- https://www.lookuptax.com/docs/tax-identification-number/japan-tax-id-guide (T-number format, lookup sites, NTA example corporate number)

## Confidence notes
- 70%/50%/30% schedule taken from NTA's Sept 2026 reform page; the statute text itself was not read.
- Check-digit formula is from general knowledge of the Corporate Number ordinance; I verified it only against the example 7000012050002 from a secondary source. Sole-trader T-numbers may not follow this check digit — keep as warning only.
- Not verified this session: 7-year retention, rounding-once-per-rate rule, JPY 10,000 return-invoice exemption, JPY 1 billion annual cap on transitional credit per non-registered supplier (2024 reform), reverse-charge 95% condition, filing deadlines, foreign-currency rules.
