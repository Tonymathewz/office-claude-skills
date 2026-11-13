# Module 2: Sales invoices and credit notes

Goal: every invoice the business issues has every field its country requires, a unique number in an unbroken sequence, correct tax, and a matching row in `sales-register.csv`.

## Before you start
- Read `setup.md`: the business's legal name, address, tax ID, registration type and invoice number format.
- Read the business's country profile. If the profile says **e-invoicing / clearance is mandatory** for this business (e.g. a government platform must approve or sign the invoice), stop. Prepare the invoice data for the user to enter in their certified system. Never produce a PDF that looks like a cleared e-invoice, and never invent a QR code, IRN, UUID, signature or clearance number.
- Check the registration type. Some types must not show tax at all (e.g. small-business exemptions). The profile says what wording to use instead.

## Create an invoice

1. **Collect the details** from the user, the quote, the job sheet or the order: customer (from `customers.csv` if known), customer tax ID for B2B, what was supplied, quantity, unit price, supply date, and payment terms.
2. **Number it.** Take the next number in the series from `sales-register.csv`. Never reuse or skip a number. If a number was used by mistake, it stays in the register as `VOID` with a reason. It is never deleted or reused.
3. **Work out the tax** per line using the profile's rates. For cross-border B2B, apply the profile's reverse-charge or zero-rating rule and its required wording. When the treatment isn't clear-cut, mark it `ASK ACCOUNTANT` and don't issue until it's answered.
4. **Check against the profile's required-fields list.** Every field present, no placeholders left.
5. **Preview** the full invoice (all fields, all lines, the totals per rate) and the register row. Wait for approval.
6. **Produce it** after approval, as a clean PDF or Word document. It should print well in black and white, with the business's logo if `setup.md` has one, and the language(s) the profile requires.
7. **Record it**: add the row to `sales-register.csv` with status `ISSUED`, file a copy in `documents/<YYYY-MM>/sales/`, and log it.
8. **Hand it over.** Give the user the file and a short covering email draft. The user sends it.

## Credit notes (and debit notes)

A credit note corrects or cancels an invoice. Never edit an issued invoice.

1. Identify the original invoice (number and date). A credit note must refer to it.
2. Give the credit note its own number (a separate series if the profile or `setup.md` says so).
3. Use the same tax rates as the original lines being credited.
4. Check the profile's time limit for issuing credit notes.
5. Preview, approve, produce, record (status `CREDIT`, linked to the original), log.
6. Update the original invoice's balance in the register (see Module 3).

## Recurring invoices
For monthly invoices (rent, contracts), keep a list in `setup.md`. Each month, prepare all of them in one preview for approval. Never issue them automatically.

## Checks before any invoice leaves the office
- [ ] Number is next in sequence, not used before
- [ ] Every field required by the profile is present
- [ ] Customer tax ID present when the profile requires it (usually B2B)
- [ ] Lines x prices = net per rate; tax per rate correct; totals correct
- [ ] Right wording for exempt, zero-rated, reverse charge or small-business status
- [ ] Currency shown; local-currency tax amount shown if the profile requires it
- [ ] Not a mandatory e-invoice case (or the user is using their certified system)
