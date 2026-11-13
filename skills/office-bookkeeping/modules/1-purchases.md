# Module 1: Purchase invoices, receipts and expense claims

Goal: every supplier document is read correctly, checked, filed as a renamed copy, and listed once (and only once) in `purchases-register.csv`, with a clear answer to "can the business claim the tax on this?"

## Steps

### 1. Collect
List the new documents in the inbox folder (PDF, image, email attachment, photo). Skip files already in the register (same file hash) and say how many were skipped.

### 2. Read each document
Extract these fields, each with a confidence mark (`OK` / `CHECK` / `UNREADABLE`) and its location in the document:

| Field | Notes |
|---|---|
| document type | tax invoice, simplified invoice/receipt, credit note, debit note, pro-forma (NOT a tax invoice), statement (NOT an invoice), quote (NOT an invoice) |
| supplier name, address, tax ID | |
| buyer name and tax ID as shown | must match `setup.md` for the tax to be claimable in most countries |
| invoice number, issue date, supply date | |
| currency | never assume; if no symbol or code is shown, mark `CHECK` |
| lines | description, quantity, unit price, tax rate per line |
| net, tax and gross **per tax rate** | a receipt with mixed rates must keep them separate |
| totals | net total, tax total, gross total |
| payment terms, due date, bank details | compare bank details with `suppliers.csv` |
| e-invoice markers | QR code, IRN, UUID, clearance number, as required by the country profile. Only record whether they are present and readable. Never create or "fix" them. |

Pro-formas, statements and quotes are never entered as purchases. Put them in `review/` with the reason.

### 3. Check
Run these for every document and list every failure:

1. **Arithmetic** (safety rule 6).
2. **Required fields** for a tax invoice in the *supplier's* country profile. Missing fields usually mean the tax can't be claimed: set `tax_claimable = NO - <missing field>` or `ASK ACCOUNTANT`.
3. **Buyer details** match the business (name, tax ID). A mismatch is a claim risk.
4. **Tax ID format** matches the country's pattern. Suggest the official online check (from the profile) for new suppliers. Don't claim it was verified unless the user confirms they checked.
5. **Rate sanity**: the rate shown exists in that country's profile.
6. **Reverse charge / cross-border**: if the supplier is abroad, apply the profile's reverse-charge or import rules and flag `ASK ACCOUNTANT` if unsure.
7. **Duplicate check** (fuzzy, not just identical files). Flag as a possible duplicate when another register row has:
   - the same supplier AND the same invoice number (ignore spaces, dashes, leading zeros, letter case), or
   - the same supplier AND the same gross amount AND an issue date within 7 days, or
   - the same gross amount AND the same invoice number from a supplier with a very similar name.
   A corrected invoice that replaces an earlier one must be linked to it, and the earlier one marked `REPLACED`. Never let both stay payable.
8. **Fraud signals** (safety rule 10): changed bank details, a new supplier with an urgent tone, a lookalike email domain, an invoice for goods or services nobody in `setup.md` recognises.
9. **Period**: the invoice date belongs to the month being processed. If not, say which month it belongs to.
10. **Foreign currency**: record the exchange rate, its date and its source (as the country profile requires, e.g. central bank rate on the invoice date). Never pick a rate without saying where it came from.

### 4. Categorise
Suggest an expense category from `suppliers.csv` history first, then from the description. Mark suggestions `CHECK` when the supplier is new. Keep categories simple (e.g. fuel, repairs, rent, utilities, office supplies, phone/internet, insurance, professional fees, travel, meals, bank charges, other) unless the accountant gave a chart of accounts in `setup.md`.

### 5. Preview
Show one table, problems first:

| # | File | Supplier | Inv no. | Date | Currency | Net | Tax | Gross | Claimable? | Flags | New file name |
|---|---|---|---|---|---|---|---|---|---|---|---|

Under the table, list each flag in plain words, e.g. "Row 3: VAT number of the buyer is missing, so the VAT may not be claimable. Ask the supplier to reissue the invoice."

### 6. Apply after approval
For approved rows only:
- copy the file to `documents/<YYYY-MM>/purchases/` named `YYYY-MM-DD Supplier InvoiceNo Gross-CUR.pdf` (safe characters only)
- add the row to `purchases-register.csv` with status `NEW` (or `APPROVED` if the user approved it for payment)
- add or update the supplier in `suppliers.csv` (never overwrite bank details; add a new line with the date and mark it `UNVERIFIED`)
- write each change to `change-log.csv`
- move nothing out of the inbox; mark processed files in the log instead

### 7. Payment list (only when asked)
List approved, unpaid invoices due by a date the user gives, oldest first. Exclude anything with a duplicate, fraud or `UNVERIFIED` bank flag and list those separately. This is a list for the person who pays. You never pay.

## Expense claims and petty cash
Treat each receipt like a purchase document with `paid_by = <employee>` or `paid_by = petty cash`. A claim total must equal the sum of its receipts. For petty cash, opening balance + top-ups - receipts = counted cash. Show any difference. Never hide it in "other".
