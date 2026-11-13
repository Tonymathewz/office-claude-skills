# Thailand (TH) — invoice & bookkeeping profile

> Last checked: 2026-11-13. Rules change often. Not tax advice: confirm anything important with a local accountant or the tax authority.

## At a glance
| Item | Value |
|---|---|
| Tax name | Value Added Tax (VAT, ภาษีมูลค่าเพิ่ม) |
| Tax authority | The Revenue Department (RD) — https://www.rd.go.th |
| Rates | **7%** (statutory 10% reduced by royal decree; Royal Decree No. 807 of 20 Aug 2026 extends 7% to **30 Sep 2027**); 0% for exports; exempt categories (e.g. basic agricultural products, healthcare, education) |
| Registration threshold | Turnover over THB 1.8 million/year |
| Currency | THB. Foreign-currency invoices must also show the baht equivalent (Bank of Thailand reference rate, applied consistently) |
| Tax ID name & format | 13-digit Taxpayer Identification Number + 5-digit branch number (`00000` = head office). Regex: `^\d{13}$`, branch `^\d{5}$` |
| Online tax-ID check | RD VAT registrant search on rd.go.th (by TIN/name) |
| Filing frequency & deadline | Monthly VAT return **PP.30**, by the 15th of the following month (extra days if e-filed); each branch files separately unless approved to consolidate |
| Record retention | At least 5 years (copy tax invoices kept with reports) |

## Full tax invoice: required fields
Issue immediately on delivery of goods; for services, immediately on receipt of payment. At least 2 copies (original to buyer, copy kept).
1. The words **"ใบกำกับภาษี" / "Tax Invoice"** clearly visible
2. Seller's name, address and **13-digit tax ID**
3. Seller's **head office / branch number** (*often missed*)
4. Buyer's name and address
5. Buyer's tax ID and head-office/branch number when the buyer is VAT-registered (*often missed* — needed for input-VAT claim)
6. Serial number of the invoice (and book number, if any)
7. Date of issue
8. Name, type, quantity and value of goods/services
9. **VAT amount shown separately** from the value
10. Thai language (and Thai baht) — foreign-language invoices need prior Director-General approval

## Simplified invoice / receipt
**Abbreviated tax invoice (ABB)**: only for VAT-registered retailers selling directly to consumers and mass-service providers (restaurants, hotels, cinemas). Cash-register (POS) ABBs need RD approval. Fields: "Tax Invoice (Abbreviated)", seller name/abbreviation and tax ID, serial number, description/quantity/value, statement that VAT is included, date. **Input VAT on an ABB is NOT claimable** by the buyer — a VAT-registered buyer must request a full tax invoice, which the seller must issue on request.

## Credit and debit notes
Treated as tax documents. Must show: "Credit Note"/"Debit Note" title, seller & buyer names, addresses, tax IDs and branch numbers, serial number and date, **original tax invoice number/date and value**, the corrected value, the difference and the VAT on the difference, and the reason. Issue in the month of the event (or the following month).
Cancelling a full invoice: retrieve original, mark cancelled, issue a new one with the same date and record in that month's report.

## E-invoicing / clearance status (as of last-checked date)
- **e-Tax Invoice & e-Receipt**: voluntary. Structured XML (ETDA standard) with digital signature; data sent to RD monthly (by the 15th of the following month). Covers tax invoices, receipts, debit/credit notes.
- **e-Tax Invoice by Email**: simplified route for businesses with revenue up to THB 30 million — PDF sent via RD-registered email service (time-stamped by ETDA).
- **No legislated mandatory B2B e-invoicing for 2026 or 2027** (reporting, not clearance).
- **The skill must NOT** fabricate digital signatures, RD reference numbers or ETDA time-stamps, or describe a PDF as an "e-Tax Invoice" unless the user issued it through an RD-registered e-Tax system.

## Numbering & language
- Sequential serial numbers (book/running numbers allowed); per branch series common.
- Thai language and THB required unless RD approval for a foreign language/currency; bilingual layouts common (Thai content must be complete).

## Reverse charge, imports & cross-border
- Services from abroad used in Thailand: Thai recipient **self-assesses 7% VAT** (form **PP.36**) and pays by the 7th of the following month; creditable as input tax in the following month.
- Foreign e-service providers selling B2C register for VAT (e-Service VAT).
- Import VAT collected by Customs.

## Checks the skill must run for this country
- VAT computed at 7% (flag 10% or other rates; flag 7% if the user's period is after 30 Sep 2027 without a further extension).
- Purchase document used for input VAT is a **full** tax invoice — flag ABBs, receipts or quotations.
- Seller and buyer tax IDs are 13 digits; branch numbers are 5 digits; buyer TIN/branch match the user's company record.
- Title "ใบกำกับภาษี"/"Tax Invoice" present; VAT shown separately.
- Foreign-currency invoices show THB equivalents.
- Credit/debit notes reference original invoice number and show difference + VAT on difference.
- Foreign services paid: PP.36 self-assessment reminder.
- Input VAT claimed within the allowed window (generally within 6 months of the invoice month) — flag older invoices.

## Common mistakes
- Accepting abbreviated invoices from restaurants/retail for input-VAT claims.
- Missing buyer branch number ("Head office 00000").
- English-only invoices without RD approval.
- Forgetting PP.36 on overseas software subscriptions.

## Sources
- https://www.thailand.go.th/event-detail/006_124
- https://flowaccount.com/blog/abbreviated-tax-invoice-in-thailand/
- https://invoicedataextraction.com/blog/thailand-tax-invoice-requirements
- https://www.hlbthai.com/cabinet-approves-1-year-extension-of-7-vat-rate-until-30-september-2027/
- https://www.fiscal-requirements.com/news/5729

## Confidence notes
- rd.go.th pages were not fetched; full-invoice fields from the Thai government portal (thailand.go.th) plus secondary sources.
- 7% extension to 30 Sep 2027 (Royal Decree 807) from HLB Thailand; confirm in the Royal Gazette.
- THB 1.8m threshold, PP.30 deadline/e-filing extension, PP.36 deadline, 6-month input-VAT window and credit-note particulars are background knowledge, not verified this session.
- e-Tax status (voluntary; THB 30m limit for email route) from one secondary source; incentive extension to 2027 reported as approved but rules pending.
