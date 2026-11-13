# Module 5: Month-end pack for the accountant

Goal: one tidy folder the accountant can work from without asking twenty questions, plus a clear list of the questions they *do* need to answer.

## Before building the pack: the close checklist
Run this and show the results. Anything not done is listed in the pack as "open".

- [ ] All purchase documents for the month processed (Module 1); review list empty or explained
- [ ] All sales invoices and credit notes for the month recorded (Module 2); sequence has no gaps (VOIDs explained)
- [ ] Payments received allocated (Module 3)
- [ ] Every bank and card account reconciled to zero difference (Module 4)
- [ ] Petty cash counted and balanced (if used)
- [ ] Missing receipts list followed up (what's still missing)
- [ ] Duplicate and fraud flags resolved
- [ ] Foreign-currency documents have rate, date and source recorded

## Build the pack
Create `packs/<YYYY-MM>/` containing:

1. **00-summary** (one page, PDF or Word, black-and-white friendly):
   - period, business, prepared by, date
   - totals: sales (net / tax / gross), purchases (net / tax / gross), bank balances per account
   - tax summary **per rate** (output tax on sales, input tax on purchases split into claimable / not claimable / ask accountant). The layout follows the country profile, but it's a working summary, not a filed return.
   - counts: documents processed, flagged, still missing
   - open items from the checklist
2. **01-sales-register** (CSV + Excel): every invoice and credit note in number order.
3. **02-purchases-register** (CSV + Excel): every purchase document, with claimable status and flags.
4. **03-bank-reconciliations**: one sheet per account, with the closing check and the matching list.
5. **04-missing-documents**: missing receipts, unallocated receipts, invoices with fields missing.
6. **05-questions-for-accountant**: numbered, each with the document, amount and a precise question, e.g. "Q3. Invoice 2026-118 from a supplier in Italy, EUR 640.00 for software: reverse charge on our side? It shows no VAT."
7. **06-change-log** extract for the month.
8. **documents/**: the month's renamed copies (or a link to the folder if it's large).

## Rules
- The pack **reports** facts and flags. It doesn't decide tax treatment and doesn't file anything.
- Never change the books while building the pack. If you find a problem, stop, report it, and send the user back to the right module.
- Totals in the summary must equal the register totals. Re-add them and show the check.
- After the user confirms the pack was handed over, mark the month `CLOSED` in `setup.md`. Changes to a closed month need the user's explicit approval and are logged as `POST-CLOSE CHANGE`.

## Handover message
Draft a short email to the accountant listing what's in the pack, the number of open questions, and anything urgent (deadlines from the country profile). The user sends it.
