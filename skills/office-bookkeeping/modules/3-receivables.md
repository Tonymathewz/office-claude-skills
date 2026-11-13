# Module 3: Who owes us? (receivables and chasing)

Goal: an accurate list of unpaid invoices, payments correctly applied (including part-payments and credit notes), and polite, well-timed reminders that the user sends.

## Record payments received
For each payment (from the bank statement or the user):
1. Find the invoice(s) it pays: by reference first, then customer + exact amount, then customer + amount of several open invoices added together.
2. If it doesn't match exactly, don't force it. Possible reasons, in order:
   - part payment
   - bank charges deducted by the customer's or the receiving bank
   - withholding tax deducted (common in parts of the Middle East and Asia; check the country profile)
   - a credit note the customer already deducted
   - an overpayment
   - a payment for a different invoice
   
   Show the best explanation and ask.
3. Preview the allocation. After approval, update the invoice's `paid_amount`, `balance` and `status` (`PART-PAID`, `PAID`, `OVERPAID`) and log it.
4. Payments that can't be matched go to an "unallocated receipts" list. They are never dropped.

## The aged debtors list
Group open balances by customer and by age from the **due date**: not yet due, 1-30, 31-60, 61-90, over 90 days. Show:

| Customer | Invoices open | Not due | 1-30 | 31-60 | 61-90 | 90+ | Total | Last contact | Disputed? |
|---|---|---|---|---|---|---|---|---|---|

Credit notes and unallocated receipts reduce the customer's total and are shown separately, so nothing is hidden.

## Chasing
Default schedule (the user can change it in `setup.md`):
- **3 days before due**: friendly heads-up (optional, for customers who are often late)
- **7 days overdue**: polite reminder with the invoice attached
- **21 days overdue**: firmer reminder and a request for a payment date
- **45 days overdue**: final reminder, then escalate to the owner or manager. Legal action or late-payment interest is the owner's decision, never the skill's.

For each reminder, draft the email for the user to send. It includes invoice number(s), date, amount due, how to pay, and a contact name. Match the language and tone in `setup.md`. Never send it yourself.

**Don't chase:**
- invoices marked `DISPUTED` (list them with the reason and who is handling it)
- customers who promised a payment date that hasn't passed
- invoices where a credit note is pending

Record every reminder sent (by the user) in the register's `last_contact` field and in the change log.

## Disputes
When a customer disputes an invoice, mark it `DISPUTED` with the reason, the date and who raised it. The fix is usually a credit note (Module 2), not editing the invoice.
