# China (CN) — invoice & bookkeeping profile

> Last checked: 2026-11-13. Rules change often. Not tax advice: confirm anything important with a local accountant or the tax authority.

## At a glance
| Item | Value |
|---|---|
| Tax name | Value-Added Tax (增值税, VAT). VAT Law + Implementing Regulations in force from 1 Jan 2026 |
| Tax authority | State Taxation Administration (国家税务总局, STA) — https://www.chinatax.gov.cn |
| Rates | General taxpayers: 13% (most goods, processing/repair, leasing movables), 9% (e.g. transport, construction, real estate, basic telecoms, some farm goods), 6% (most modern/financial services); 0% exports. Small-scale taxpayers: 3% levy rate (simplified method, no input credit) |
| Registration threshold | Small-scale vs general taxpayer line: RMB 5 million taxable sales over a rolling 12 months / 4 quarters. Once general, cannot revert |
| Currency | RMB. Treat fapiao as RMB documents (see Confidence notes) |
| Tax ID name & format | Unified Social Credit Code (统一社会信用代码, USCC) used as taxpayer ID: 18 characters, digits + uppercase letters excluding I, O, Z, S, V. Regex `^[0-9A-HJ-NPQRTUWXY]{2}\d{6}[0-9A-HJ-NPQRTUWXY]{10}$` |
| Online tax-ID check | No reliable public taxpayer check confirmed; fapiao authenticity check via the national invoice verification platform (inv-veri.chinatax.gov.cn — not opened this session) |
| Filing frequency & deadline | General taxpayers usually monthly, small-scale often quarterly; generally by the 15th of the following month |
| Record retention | Accounting Archives Measures (MoF Order 79, from 2016): minimum 10 or 30 years depending on record type; electronic-only archiving allowed if conditions met |

## Full tax invoice: required fields
There is only one legal "invoice" in China: the **fapiao** (发票), issued through the tax system. A commercial invoice or receipt without a fapiao does not support VAT credit or (usually) a tax deduction.
Check that a received fapiao shows:
1. Fapiao type: **special VAT** (增值税专用发票 — needed to claim input VAT) or **ordinary/general** (普通发票 — no input VAT credit)
2. **20-digit fapiao number** (fully digitalised e-fapiao) — older formats used a code + 8-digit number
3. Issue date
4. **Buyer name and buyer tax ID (USCC)** exactly matching your registration (often wrong)
5. Seller name and seller tax ID
6. Goods/services description with tax classification, quantity, unit price
7. Amount excl. VAT, VAT rate, VAT amount, total in figures and in Chinese characters
8. Issuer/reviewer fields; electronic signature on e-fapiao

## Simplified invoice / receipt
- No "simplified fapiao" category. Ordinary fapiao (and certain transport tickets/e-itineraries) serve as receipts.
- Ordinary fapiao generally cannot be used for input VAT, but some passenger-transport e-tickets/e-itineraries can (see STA Announcement 2024 No. 9 for air travel).

## Credit and debit notes
- Corrections/refunds are done by a **red-letter fapiao** (红字发票), not a free-form credit note.
- For fully digitalised fapiao, a red-letter information confirmation form is raised on the e-invoice platform (by buyer or seller depending on case), then the red fapiao is issued, linked to the original.
- A blue fapiao cannot simply be "voided" once delivered and booked; never accept an edited PDF as a correction.

## E-invoicing / clearance status (as of last-checked date)
- **Fully digitalised e-fapiao (全面数字化的电子发票, 数电票) rolled out nationwide from 1 Dec 2024.** Issued free via the national e-invoicing service platform; no tax-control device (Golden Tax disk/UKey) needed.
- Each has a unique **20-digit number**: digits 1–2 year, 3–4 region code, 5 issuing channel, 6–20 sequence.
- Same legal validity as paper fapiao. Tax authority sets a monthly issuing limit per taxpayer; no per-invoice amount cap.
- Paper fapiao and older e-fapiao types still exist in parallel in some cases.
- The skill must NOT: create, edit, or "re-render" a fapiao; invent fapiao numbers; treat a scanned paper fapiao as the original; mark a fapiao verified without the user checking it on the official platform.

## Numbering & language
- Numbers are assigned by the tax platform — the business does not choose a series.
- Chinese language. Bilingual commercial invoices may accompany, but the fapiao is the tax document.

## Reverse charge, imports & cross-border
- Import VAT is paid to Customs; the customs import VAT payment certificate (not a supplier fapiao) supports the input credit.
- Payments to overseas suppliers for services consumed in China generally require the Chinese payer to withhold VAT (plus surcharges and often income tax). The new VAT Law redefines "consumed in China" — get accountant confirmation.
- A foreign company/office without a Chinese entity cannot issue fapiao; a Chinese supplier's fapiao must name the Chinese registered buyer.

## Checks the skill must run for this country
- Document is a fapiao (has 20-digit number or legacy code+number), not just a commercial invoice/proforma → otherwise flag "no fapiao: not creditable/deductible".
- Fapiao number is exactly 20 digits for 数电票 (`^\d{20}$`); first two digits plausibly match issue-date year.
- Buyer name and buyer USCC exactly equal the company master data (character-for-character).
- USCC is 18 chars and matches regex above; optional checksum (GB 32100-2015, see Confidence notes) → warning only.
- If input VAT is being claimed: fapiao type is **special** VAT fapiao and buyer is a general taxpayer; ordinary fapiao → no input VAT.
- VAT rate is one of 13/9/6/3/1/0 or exempt; VAT amount ≈ net × rate (±0.01 RMB per line).
- Rate matches the service type (e.g. consulting at 13% is suspicious → flag).
- Duplicate check on fapiao number across all months.
- Red-letter fapiao references an original fapiao number that exists in the books.
- Prompt the user to verify authenticity on the official verification platform and record the date checked.

## Common mistakes
- Buyer name/tax ID typo → fapiao unusable for credit.
- Accepting ordinary fapiao when a special VAT fapiao was needed.
- Paying overseas service invoices without withholding.
- Treating a PDF that was edited/forwarded as genuine.
- Booking the same fapiao twice (PDF + OFD/XML copies).

## Sources
- https://fgk.chinatax.gov.cn/zcfgk/c100012/c5235729/content.html (STA/MoF/CAAC Announcement 2024 No. 9: 20-digit structure, air e-itineraries as 数电票)
- https://www.china-briefing.com/news/e-invoicing-China-expansion-fully-digitalized-e-fapiao-program-details-timeline/ (nationwide rollout 1 Dec 2024, no tax-control device, limits)
- https://www.china-briefing.com/doing-business-guide/china/taxation-and-accounting/china-s-e-fapiao-system-at-a-glance (fapiao types, special vs general use, verification duty)
- https://www.roedl.com/en/insights/the-chinese-value-added-tax-law-officially-takes-effect/ (VAT Law from 1 Jan 2026, rates, RMB 5m small-scale threshold, 3%)
- https://www.gov.cn/zhengce/2015-12/11/content_5717189.htm (Accounting Archives Management Measures, MoF Order 79)

## Confidence notes
- Exact retention per document type (commonly cited: vouchers and ledgers 30 years; bank statements/reconciliations 10 years) is in the Order 79 appendix, which I did not see.
- Small-scale 1% reduced levy rate (temporary relief) — status in 2026 unverified; the skill should accept 1% but flag for accountant confirmation.
- USCC checksum (charset `0-9A-HJ-NPQRTUWXY`, weights 1,3,9,27,19,26,16,17,20,29,25,13,8,24,10,30,28, check = 31 − (Σ mod 31), 31→0) is from memory; not confirmed from the standard this session.
- Verification-platform URL inv-veri.chinatax.gov.cn could not be opened (blocked); listed but not seen.
- Filing deadline (15th), buyer-tax-ID rule for ordinary fapiao, red-letter procedure details, withholding rules and foreign-currency fapiao rules are from general knowledge, not verified this session.
