# South Korea (KR) — invoice & bookkeeping profile

> Last checked: 2026-11-13. Rules change often. Not tax advice: confirm anything important with a local accountant or the tax authority.

## At a glance
| Item | Value |
|---|---|
| Tax name | Value-Added Tax (부가가치세, VAT) |
| Tax authority | National Tax Service (국세청, NTS) — https://www.nts.go.kr (English: https://www.nts.go.kr/english/main.do); e-filing/e-invoice portal: Hometax |
| Rates | Standard 10%; 0% for exports and certain services to non-residents paid in foreign currency; exempt: e.g. unprocessed food, medical, education, financial/insurance, residential rent, books/newspapers |
| Registration threshold | No turnover threshold — every business must register (business registration). Small individuals may be "simplified taxpayers" (간이과세자) below an annual sales ceiling (raised to KRW 104 million in 2024) |
| Currency | KRW; foreign-currency amounts converted to KRW on the tax invoice (see Confidence notes) |
| Tax ID name & format | Business Registration Number (사업자등록번호, BRN): 10 digits, `XXX-XX-XXXXX`. Regex `^\d{3}-?\d{2}-?\d{5}$`. Digits 1–3 tax office, 4–5 business type (01–79 individual, 81–84 corporation…), 6–9 serial, 10 check digit |
| Online tax-ID check | NTS Hometax business status lookup (open/closed, taxpayer type) — free |
| Filing frequency & deadline | Quarterly returns/payments due within 25 days after each calendar quarter (two 6-month tax periods with preliminary returns) |
| Record retention | 5 years (tax invoices); e-tax invoices are also held in the NTS system |

## Full tax invoice: required fields
Electronic Tax Invoice (전자세금계산서). Mandatory items (필요적 기재사항) — missing any = defective invoice:
1. **Supplier BRN** and supplier name
2. **Buyer BRN** (often wrong or missing)
3. Supply value (공급가액, net)
4. VAT amount
5. **Date of preparation** (작성일자 — tax point date, not just send date)
Optional but normal: addresses, buyer name, business type/item, item description, unit price, quantity, supply date.

## Simplified invoice / receipt
- B2C and small sales use receipts (영수증), cash receipts (현금영수증) or card slips.
- Buyer can generally claim input VAT on a card slip or cash receipt (business-expense type) that shows VAT separately and the buyer's BRN for cash receipts — confirm with accountant (see Confidence notes).
- Simplified taxpayers below a lower sales level may only issue receipts, not tax invoices.

## Credit and debit notes
Done by an **amended (modified) e-tax invoice** (수정세금계산서) linked to the original's NTS approval number. Reason codes:
| Reason | How | Date / deadline |
|---|---|---|
| Error correction | negative copy of original + new positive copy | original date; when noticed |
| Price change | +/− difference only | date of change; by 10th of next month |
| Return of goods | − returned amount | return date; by 10th of next month |
| Contract cancelled | − amount | cancellation date; by 10th of next month |
| Local L/C opened later | − taxable copy + zero-rated copy | original date; by 10th/25th of next month |
| Duplicate issuance | − identical copy | original date; any time |
Amended invoice can only be raised if the original was successfully transmitted to NTS.

## E-invoicing / clearance status (as of last-checked date)
- **Mandatory e-tax invoices:** all corporations (since 2011); individual businesses with prior-year supply value ≥ KRW 80 million (from 1 Jul 2024; earlier thresholds 300m/200m/100m).
- Issue via Hometax, an ERP, or a licensed ASP; **transmit to NTS by the day after issuance.**
- Monthly consolidated invoices can be issued by the 10th of the following month.
- Penalties ~0.3%–1% of supply value for non/late issuance or late transmission.
- Each e-tax invoice gets an NTS approval number (승인번호). The skill must NOT invent approval numbers or produce a "tax invoice" PDF that pretends to be NTS-issued; it can only prepare data for the user to issue in Hometax/ERP.

## Numbering & language
- Approval number assigned by the system; internal invoice number optional.
- Korean.

## Reverse charge, imports & cross-border
- Services from non-resident suppliers without a Korean business place: buyer may need to self-pay VAT at 10% (proxy payment, 대리납부), mainly where the service is used for VAT-exempt business.
- Foreign digital service providers selling B2C must register and charge 10%.
- Import VAT is paid to Customs; customs-issued import tax invoice supports the credit.

## Checks the skill must run for this country
- Supplier and buyer BRN present, 10 digits after stripping hyphens.
- BRN checksum (warning only): weights 1,3,7,1,3,7,1,3,5 on digits 1–9; sum products, add floor(d9×5/10); check = (10 − sum mod 10) mod 10 must equal digit 10.
- Buyer BRN = our company BRN exactly.
- All five mandatory items present; preparation date is in the correct month for the supply.
- VAT = 10% of supply value (±1 KRW), or 0 with zero-rate/exempt reason stated.
- For corporate suppliers or flagged individuals: invoice is an e-tax invoice with an NTS approval number (do not validate format, just presence).
- Issue date ≤ 10th of month following supply month (if consolidated); flag late invoices.
- Amended invoice references an original approval number already in the books; negative amounts match reason.
- Duplicate check on approval number.

## Common mistakes
- Paper/PDF invoice from a supplier obliged to e-issue → input VAT at risk.
- Wrong preparation date (date sent instead of supply date).
- Using a free-form credit note instead of an amended e-tax invoice.
- Buyer BRN of a branch vs head office mismatched.

## Sources
- https://www.grantthornton.global/en/insights/indirect-tax-guide/indirect-tax---South-Korea/ (rate, zero-rating, exemptions, mandatory fields, quarterly filing, reverse charge)
- https://sovos.com/vat/tax-rules/electronic-tax-invoices-south-korea/ (e-invoice thresholds by date, one-day transmission, penalties, 5-year storage)
- https://developers.popbill.com/en/guide/taxinvoice/introduction/modified-taxinvoice (amended tax invoice reasons and deadlines)
- https://lookuptax.com/docs/tax-identification-number/korea-tax-id-guide (BRN structure)
- https://www.asiae.co.kr/en/article/2024061810023094125 (simplified taxpayer ceiling KRW 104m — headline only)

## Confidence notes
- BRN checksum algorithm is from memory; not confirmed from an official source this session — use as warning, never reject.
- Hometax URL not seen; only portal name given.
- "Consolidated by 10th of next month" seen only via amendment-deadline context; general issuance rule from knowledge.
- Simplified-taxpayer KRW 104m from headline only; lower receipt-only level and card-slip input-credit conditions not verified.
- Foreign-currency conversion rules not verified.
