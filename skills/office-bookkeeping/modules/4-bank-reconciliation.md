# Module 4: Bank and card reconciliation

Goal: every line on the bank (or card) statement is explained by a document, and the statement's closing balance is proven against the books for that month.

## 1. Read the statement safely
Statements are where AI tools most often lose a minus sign, drop a row or swap digits, so:
1. Prefer the bank's CSV or Excel export. Use a PDF only if that's all there is.
2. After reading, **prove the statement**: opening balance + money in - money out = closing balance, using the statement's own figures. Also count the lines. If it doesn't balance, stop and show the difference. Don't continue with a statement you can't prove.
3. Keep debits and credits in separate columns. Never rely on a sign alone.
4. Note the account (last 4 digits only), currency and period.

## 2. Match
Match each statement line, in this order, and record the method used:
1. **Exact**: reference or invoice number in the description + exact amount.
2. **Amount + name**: exact amount + supplier or customer name (or known alias in `suppliers.csv`/`customers.csv`) within 10 days.
3. **Group**: one line paying several invoices (sum matches), or several lines paying one invoice (part payments).
4. **Known regulars**: bank charges, interest, card fees, salaries, rent, loan repayments, tax payments. Match to the rule in `setup.md`, or ask once and remember the rule there.
5. **Differences**: amount close but not exact. Show it as `amount difference: X` with likely reasons: bank fee, exchange difference, withholding tax, discount, part payment. Never round it away.

Foreign-currency lines: show both amounts and the rate the bank used. The difference to the invoice's booked amount is an exchange difference. Show it, don't hide it.

## 3. Preview
Show three lists:
- **Matched**: line, document, method. Collapse this list if it's long.
- **Matched with a difference**: needs approval.
- **Unexplained**: money out with no receipt ("missing receipt"), money in with no invoice ("unallocated receipt"). Sorted by amount, biggest first.

## 4. Apply after approval
- Write the matching sheet to `bank/<YYYY-MM>/matching.csv`.
- Update payment status in the purchases and sales registers (`PAID` / `PART-PAID`) with the bank date and line reference.
- Log every change.

## 5. Close the month's reconciliation
Show the final check:

```
Statement closing balance          EUR  12,345.67
Less: payments in books not yet on statement   (list)
Add:  receipts in books not yet on statement   (list)
= Balance per books                 EUR  12,345.67   difference: 0.00
```

Mark the month reconciled only when the difference is zero, or the user approves the remaining difference with a written reason. The reconciliation sheet gets a "prepared by / date" line and a "reviewed by / date" line for a second person.

## Missing receipts list
For every unexplained payment out, produce a list the user can work through: date, amount, payee as shown, and a suggested action ("ask supplier for invoice", "staff card expense, collect receipt", "check if personal"). This list goes into the month-end pack.
