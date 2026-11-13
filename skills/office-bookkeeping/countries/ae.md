# United Arab Emirates (AE) - invoice & bookkeeping profile

> Last checked: 2026-11-13. Rules change often (e-invoicing is going live in 2027). Not tax advice: confirm anything important with a UAE tax agent or the Federal Tax Authority (FTA).

## At a glance
| Item | Value |
|---|---|
| Tax name | VAT (Federal Decree-Law No. 8 of 2017 and its Executive Regulation) |
| Tax authority | Federal Tax Authority (FTA), https://tax.gov.ae/en/ ; e-invoicing policy by the Ministry of Finance (MoF), https://mof.gov.ae |
| Rates | 5% standard; 0% zero-rated (e.g. exports, some education/healthcare); exempt (e.g. some financial services, residential property, local passenger transport) |
| Registration threshold | Mandatory above AED 375,000 taxable supplies a year; voluntary above AED 187,500 (see confidence notes) |
| Currency | AED. Foreign-currency invoices allowed, but tax amount must be shown in AED with the exchange rate used (UAE Central Bank rate) |
| Tax ID name & format | TRN (Tax Registration Number): 15 digits, starts with `100`, no letters. Regex `^100\d{12}$` |
| Online tax-ID check | EmaraTax "TRN Verification" (no login), https://eservices.tax.gov.ae |
| Filing frequency & deadline | Usually quarterly (FTA may set monthly). Return and payment due within 28 days after the period ends |
| Record retention | At least 5 years from end of the tax period (VAT Law Art. 70); 15 years for real estate records |

## Full tax invoice: required fields
1. The words "Tax Invoice" clearly shown
2. Supplier name, address and TRN
3. Recipient name, address and TRN (when recipient is VAT-registered) - **often missed**
4. Unique sequential invoice number
5. Date of issue, and date of supply if different - **often missed**
6. Description of goods/services
7. Per line: quantity, unit price, tax rate, amount payable in AED
8. Any discount
9. Gross amount, tax amount in AED
10. Exchange rate if not in AED - **often missed**
11. If reverse charge applies: a statement that the recipient must account for the tax, with the legal reference
- Issue within 14 days of the date of supply. Wholly zero-rated supplies still need a tax invoice.

## Simplified invoice / receipt
- Allowed where the recipient is not VAT-registered, or where the recipient is registered and the consideration is AED 10,000 or less (see confidence notes).
- Minimum fields: "Tax Invoice", supplier name, address and TRN, date, description, total and tax amount.
- Not allowed for reverse-charge supplies.
- **Once a business is inside e-invoicing, simplified tax invoices are no longer allowed** for its in-scope (B2B/B2G) supplies; the full FTA data set is required regardless of value.
- For input VAT, prefer a full tax invoice showing the buyer's TRN; a simplified invoice over AED 10,000 to a registered buyer is a flag.

## Credit and debit notes
- Title "Tax Credit Note"; must reference the original invoice number and date, state the reason, and show the VAT adjustment.
- Supplier and recipient adjust VAT in the period the note is issued.
- Under e-invoicing, credit notes also go through the ASP as e-credit notes.

## E-invoicing / clearance status (as of 2026-11-13)
- **System:** national Electronic Invoicing System, Peppol-based five-corner decentralised model (DCTCE). Each in-scope business must appoint one MoF-accredited service provider (ASP). Format: PINT-AE. Invoices are exchanged ASP-to-ASP and tax data is reported to the FTA.
- **Scope:** B2B and B2G (and G2B/G2G). **B2C is excluded** until a later ministerial decision. Exclusions include sovereign government activity, some international air transport, and exempt/zero-rated financial services. Intra-tax-group transactions excluded for 24 months from 1 Jan 2027.
- **Phases (Ministerial Decision 244/2025, as amended):**
  | Group | Appoint ASP by | Go-live |
  |---|---|---|
  | Pilot / voluntary | from 1 Jul 2026 | voluntary |
  | Revenue >= AED 50m | 30 Oct 2026 (extended from 31 Jul 2026) | **1 Jan 2027** |
  | Revenue < AED 50m | 31 Mar 2027 | **1 Jul 2027** |
  | Government entities | 31 Mar 2027 (one source says 31 Jul 2027) | 1 Oct 2027 |
- **Effect on purchases:** where e-invoicing applies, a paper/PDF copy is not enough for input VAT recovery; the structured e-invoice received via the ASP is the valid invoice.
- **Peppol ID:** VAT-registered participants use scheme `0235` + first 10 digits of the TRN.
- **Penalties:** e.g. AED 5,000/month for not appointing an ASP; AED 100 per e-invoice not issued/transmitted correctly (capped AED 5,000/month).
- **The skill must NOT fake:** Peppol message IDs, ASP validation status, or any "transmitted to FTA" confirmation. For in-scope sales, tell the user to issue through their ASP/ERP; the skill can only draft the invoice data for them to enter.

## Numbering & language
- Unique, sequential numbering; separate series per branch/document type is acceptable if each is sequential.
- English is accepted on invoices; the FTA may ask for an Arabic translation (see confidence notes).

## Reverse charge, imports & cross-border
- Imported services/goods from abroad: the UAE registered recipient self-accounts (reverse charge) in its return.
- Since 1 Jan 2026 the recipient no longer issues a self-invoice for reverse charge, but must keep supporting documents (supplier invoice, contract, payment proof).
- A UAE supplier applying reverse charge must state it on the invoice.

## Checks the skill must run for this country
- Supplier TRN present, 15 digits, matches `^100\d{12}$`; otherwise `CHECK`. Remind user to verify on EmaraTax and keep a dated screenshot for new suppliers.
- Document titled "Tax Invoice" (or "Tax Credit Note"); a "Proforma", "Quotation" or "Delivery note" is not a tax invoice.
- VAT rate is 5% or 0%; any other rate = flag. Check VAT = net x 5% (rounding 0.01 per line).
- Buyer's name and TRN shown when our business is VAT-registered and amount > AED 10,000; otherwise flag "simplified invoice over AED 10,000".
- Foreign-currency invoice: VAT amount shown in AED and exchange rate stated.
- Invoice date within 14 days of supply date where both are shown; else note.
- Purchase dated on/after the supplier's go-live date (1 Jan 2027 or 1 Jul 2027) and only a PDF received: flag `ASK ACCOUNTANT - e-invoice via ASP needed for VAT recovery?`
- Sales: if our business is in e-invoicing scope and go-live has passed, do not issue a PDF tax invoice; tell the user to issue it through their ASP.
- Foreign supplier, no VAT charged: flag reverse charge; `ASK ACCOUNTANT` if unsure.

## Common mistakes
- Missing buyer TRN on B2B invoices; missing AED VAT amount on USD/EUR invoices.
- Treating a proforma or payment receipt as a tax invoice.
- Using the trade-licence number in place of the TRN.
- Accepting VAT invoices from a supplier whose TRN shows deregistered on EmaraTax.
- Assuming B2C is in e-invoicing scope (it is not yet).

## Sources
- https://mof.gov.ae/wp-content/uploads/2025/09/Ministerial-Decision-No.-244-of-2025-on-the-Implementation-of-the-Electronic-Invoicing-System.pdf
- https://mof.gov.ae/en/news/ministry-of-finance-announces-targeted-amendments-to-einvoicing-system-decisions/
- https://thenationalnews.com/business/2026/10/19/uae-amends-e-invoicing-regulations-as-implementation-deadline-draws-closer
- https://www.fiscal-requirements.com/news/5357-uae-e-invoicing-legal-framework-and-implementation-updated-2026
- https://kpmg.com/ae/en/insights/tax-insights/implementation-of-the-electronic-invoicing-system-in-the-uae.html
- https://www.crowe.com/ae/news/what-is-the-recent-amendment-to-uae-vat
- https://www.pwc.com/m1/en/tax/documents/2026/gcc-indirect-tax-news-roundup-q3-2026.pdf
- https://www.meydanfz.ae/blog/uae-tax-invoice-requirements
- https://www.middleeastbriefing.com/news/what-to-do-after-vat-registration-uae-guide-for-companies/
- https://bcl.ae/blogs/trn-verification-uae/

## Confidence notes
- Registration thresholds (AED 375,000 / 187,500) not confirmed on a page read for this file.
- Simplified-invoice threshold: sources disagree on wording (AED 10,000 limit for registered recipients vs "supplies under AED 10,000"). The FTA-approved simplified-invoice regime was not read on tax.gov.ae directly.
- Government-entity ASP deadline: 31 Mar 2027 in the original MD 244/2025; PwC Q3 2026 says 31 Jul 2027 (possible later amendment).
- No rule found on the deadline for transmitting e-invoices; KPMG says normal VAT timelines apply.
- Arabic-translation-on-request and the "Tax Credit Note" title are from general knowledge/secondary sources.
- PwC Q3 2026 also mentions supplier verification under FTA Decision 13 of 2026 (from 1 Oct 2026) and Cabinet Decision 149 of 2026 amendments; contents not reviewed. Ask the accountant whether they change purchase checks.
