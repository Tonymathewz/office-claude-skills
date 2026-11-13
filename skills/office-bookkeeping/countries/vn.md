# Vietnam (VN) — invoice & bookkeeping profile

> Last checked: 2026-11-13. Rules change often. Not tax advice: confirm anything important with a local accountant or the tax authority.

## At a glance
| Item | Value |
|---|---|
| Tax name | Value Added Tax (VAT, Thuế giá trị gia tăng – GTGT) |
| Tax authority | General Department of Taxation / Tax Department, Ministry of Finance — https://www.gdt.gov.vn |
| Rates | 10% standard; **temporarily 8%** for many 10%-rated goods/services **1 Jul 2025 – 31 Dec 2026** (Resolution 204/2025/QH15, Decree 174/2025); 5% (essentials); 0% (exports); exempt. Excluded from the 8% cut: telecoms, real estate, finance/banking/securities/insurance, and other listed sectors |
| Registration threshold | Enterprises: all register. Household/individual businesses exempt from VAT if annual revenue ≤ VND 500 million (from 1 Jan 2026) |
| Currency | VND; foreign currency allowed where permitted, with exchange rate shown |
| Tax ID name & format | Tax code (MST): **10 digits** for independent enterprises/organisations; **13 digits** (`10 digits-3 digits`) for dependent units/branches; individuals & household businesses use the **12-digit personal identification number** (since 1 Jul 2025). Regex: `^\d{10}(-\d{3})?$` or `^\d{12}$` |
| Online tax-ID check | GDT taxpayer lookup (tracuunnt.gdt.gov.vn) |
| Filing frequency & deadline | Monthly (20th of following month) or quarterly (last day of first month of next quarter) depending on size |
| Record retention | 10 years for accounting documents/invoices |

## Full tax invoice: required fields
All invoices must be **e-invoices** (Decree 123/2020 as amended by **Decree 70/2025**, effective 1 Jun 2025).
1. Invoice name (e.g. "HÓA ĐƠN GIÁ TRỊ GIA TĂNG"), form symbol, invoice symbol and invoice number
2. Seller name, address, **tax code**
3. Buyer name, address, **tax code** / budget-relationship code / **personal identification number** (individuals) — *often missed*
4. Goods/service names **in Vietnamese** (foreign language allowed in brackets or alongside), unit, quantity, unit price
5. Amount before VAT, **VAT rate** per line, VAT amount, total payable (figures and words)
6. Seller digital signature (and buyer's where applicable); date of signature
7. Date of issue (= time of invoicing rule below)
8. **Tax authority code** (for "invoices with code") or the invoice data transmitted (for "without code")
9. When the 8% rate is used: show **8%** as the rate (or for direct-method sellers, the 20% reduction note)

**Time of issue**: goods — at transfer of ownership/right of use, regardless of payment; services — on completion, or on collection if paid in advance (deposits excluded).

## Simplified invoice / receipt
No paper "simplified" invoice. Retail/F&B/hotel/transport/personal services and household businesses with revenue ≥ VND 1 billion use **e-invoices generated from cash registers (POS)**: seller name, address, tax code, items, amount, time of issue, plus tax-authority code/data. Buyer info only if the buyer requests it (name, address, tax code/personal ID/phone). Delivered electronically, via link or QR code. A business buyer wanting to claim input VAT should request its tax code on the invoice.

## Credit and debit notes
Errors are fixed by **adjustment invoices** or **replacement invoices** (Article 19, Decree 70/2025) — not by editing the original. Seller and buyer must first sign a **written agreement identifying the error** (for individual buyers: notify them or post on website). Adjustments to tax code, amount, rate or goods are declared in the period the adjusting invoice is issued (seller) / received (buyer).

## E-invoicing / clearance status (as of last-checked date)
- **Mandatory for all** enterprises and business households since 1 Jul 2022.
- Two types: **e-invoice with tax authority code** (clearance — the tax authority assigns a code before the invoice is sent to the buyer) and **without code** (eligible businesses; data must be transmitted to the tax authority **no later than the following working day**).
- Cash-register e-invoices must be connected to the tax authority.
- **The skill must NOT** fabricate tax-authority codes, invoice symbols/numbers, digital signatures, lookup codes or QR codes. Users must issue via their registered e-invoice provider/GDT portal; the skill may draft data and verify.

## Numbering & language
- Invoice numbers are sequential within each invoice symbol, assigned by the e-invoice system; no gaps.
- Vietnamese required; foreign text only in parentheses or next to Vietnamese.

## Reverse charge, imports & cross-border
- Services from foreign suppliers without PE: Vietnamese buyer withholds **Foreign Contractor Tax** (VAT + CIT portions) and declares it; foreign e-commerce/digital suppliers register/declare VAT (10%) or platforms withhold.
- Import VAT collected by Customs.
- Exports 0% with contract, non-cash payment and customs evidence.

## Checks the skill must run for this country
- Seller tax code matches `^\d{10}(-\d{3})?$` (or 12-digit personal ID for households); buyer tax code on purchase invoices equals the user's tax code.
- Document is an e-invoice with invoice symbol, number and (if "with code") a tax-authority code; scanned paper/PDF quotations → flag.
- VAT rate per line is 0/5/8/10%; if 8% is used, invoice date is between 1 Jul 2025 and 31 Dec 2026 and the item is not in an excluded sector; flag 8% on telecoms/real estate/finance. For invoices dated from 1 Jan 2027, flag 8% unless the user confirms a new extension.
- Purchases ≥ VND 5 million (incl. VAT): **non-cash payment evidence** is required for input-VAT deduction — check bank payment matches during reconciliation.
- Goods/service names are in Vietnamese.
- Corrections: adjustment/replacement e-invoice references the original and a written error agreement exists.
- Invoice date matches the time-of-issue rule (goods: delivery/ownership transfer; services: completion or prepayment).
- Never treat a lookup code or QR as valid unless copied from the user's e-invoice system.

## Common mistakes
- Paying ≥ VND 5m in cash → input VAT not deductible.
- Applying 8% to excluded sectors, or continuing 8% after it lapses.
- Buyer tax code/name wrong on supplier invoice.
- Cancelling and reissuing instead of the proper adjustment/replacement process.
- Late invoice issue (e.g. waiting for payment for goods).

## Sources
- https://www.dfdl.com/insights/legal-and-tax-updates/vietnam-extension-of-the-reduced-8-vat-rate-to-31-december-2026/
- https://www.vietnam-briefing.com/news/decree-70-key-amendments-to-invoice-regulations-in-vietnam.html/
- https://thuvienphapluat.vn/van-ban/EN/Thue-Phi-Le-Phi/Decree-70-2025-ND-CP-amendments-Decree-123-2020-ND-CP-prescribing-invoices-and-records/650854/tieng-anh.aspx?tab=0
- https://www.vietnam-briefing.com/news/vietnam-new-vat-law-key-compliance-guidance.html/
- https://www.pwc.com/vn/en/publications/news-brief/250224-new-rules-on-tax-code.html
- https://luatvietnam.vn/legal-updates/new-tax-registration-rules-from-july-1-2026-892-110256-article.html

## Confidence notes
- gdt.gov.vn was not fetched; sources are law firms and legal databases.
- **8% reduction ends 31 Dec 2026** under current law; no 2027 extension found as of 13 Nov 2026 — re-check in Dec 2026.
- Circular 90/2026/TT-BTC (effective 1 Jul 2026) replaced Circular 86/2024 on tax registration; tax-code formats (10/13 digits, personal ID for individuals) assumed unchanged — verify.
- VND 5m non-cash rule: source says non-cash receipts are required for purchases ≥ VND 5m; linkage to input-VAT deduction is from VAT Law 48/2024 as commonly reported.
- Full invoice-content list (Article 10 Decree 123) only partly visible; filing deadlines, 10-year retention, FCT and export conditions are background knowledge.
- Household VAT exemption threshold VND 500m from 1 Jan 2026 from one secondary source.
