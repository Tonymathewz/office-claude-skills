---
name: office-bookkeeping
description: Use for small-office accounts work done by non-accountants anywhere in the world - checking and filing supplier invoices and receipts, issuing sales invoices and credit notes, chasing unpaid invoices, matching bank statements, and preparing the month-end pack for the external accountant. Works with plain folders and spreadsheets (no accounting software needed), applies the right country's invoice and VAT/GST rules, and never changes, pays or sends anything without the user's approval.
---

# Office bookkeeping

Help office staff keep clean, checkable books and hand a tidy pack to their accountant every month. You prepare and check. The user approves. The accountant decides on tax treatment.

## Safety rules (apply to every module, no exceptions)

1. **Never invent a figure.** Every number you write must come from a document the user gave you. Record where it came from (file name + page/line). If a value can't be read, write `UNREADABLE` and ask. Never fill a gap with a guess, a "typical" value, or a file's modified date.
2. **Preview, then approve, then apply.** Before creating, renaming, moving or editing any file or record, show a preview table. Apply only the rows the user approves.
3. **Never pay, send, post or delete.** You draft payment lists, emails and reminders. The user sends and pays. Never delete a document; mark it `VOID` or `DUPLICATE` instead.
4. **Originals are untouchable.** Work on copies. Never edit, overwrite or move an original file.
5. **Log every change** in `books/change-log.csv`: date-time, module, what changed, old value, new value, source document, approved by.
6. **Check the arithmetic** on every document: lines add up to net, net + tax = gross, tax = net x rate (allow rounding of 0.01 per line, and say so when used). A failed check is a flag, not something to fix silently.
7. **Show confidence.** Mark every extracted field `OK` (clearly read), `CHECK` (read but unsure: blurred, handwritten, ambiguous) or `UNREADABLE`. Any document with a `CHECK` or `UNREADABLE` amount, date, tax ID or currency goes to the review list.
8. **Dates and numbers are traps.** Decide day-first vs month-first from the country profile and the document itself, and say which you used when it's ambiguous (e.g. 05/06). Watch decimal commas (`1.234,50` vs `1,234.50`), minus signs, brackets for negatives, and `CR`/`DR` markers.
9. **One period at a time.** Finish and reconcile one month before starting the next, so errors don't snowball.
10. **Fraud check before any payment list.** A supplier's bank details that differ from the ones on record, a new supplier asking for urgent payment, or a lookalike email address must be flagged in capitals: `VERIFY BY PHONE ON A KNOWN NUMBER BEFORE PAYING`. Never take the phone number from the suspicious email or invoice.
11. **Not tax advice.** Apply the country profile's checks, but when the treatment is unclear (exempt or not, reverse charge or not, claimable or not), mark it `ASK ACCOUNTANT` with the exact question. Never guess the tax treatment.
12. **Private data stays private.** Don't send document contents to outside services unless the user set that up. Mask full bank account and card numbers in summaries (show the last 4 digits only).

## First run: set up the books

If `books/setup.md` doesn't exist, create it from `templates/setup.md` by asking the user only what's missing:
- business name, country (and state/emirate/province where it matters), tax registration type and tax ID
- base currency, financial year start, invoice number format for sales
- where documents arrive (folder) and where the books folder should live
- the accountant's name and how often they want the pack (usually monthly)
- who approves payments (a different person from who prepares them, if the office has two people)

Then create the books folder from `templates/`:

```
books/
  setup.md
  change-log.csv
  suppliers.csv            (supplier name, tax ID, bank details last verified + date, usual category)
  customers.csv
  purchases-register.csv
  sales-register.csv
  bank/<YYYY-MM>/          (statements as received + matching sheet)
  documents/<YYYY-MM>/purchases/  and  /sales/   (renamed COPIES)
  review/                  (anything waiting for the user)
  packs/<YYYY-MM>/         (month-end packs)
```

## Load the country rules

Read `countries/<code>.md` for the business's country (ISO code, lowercase, e.g. `ae`, `in`, `mt`). For EU countries also read `countries/eu.md`. For a supplier or customer in another country, read that country's file too when checking cross-border documents. If there is no file for the country, use `countries/_generic.md` and tell the user the checks are basic.

Load only the files you need. Don't read every country.

Available profiles:
- **Middle East:** `ae` UAE, `sa` Saudi Arabia, `bh` Bahrain, `om` Oman, `qa` Qatar, `kw` Kuwait, `eg` Egypt
- **South Asia:** `in` India, `pk` Pakistan, `bd` Bangladesh, `lk` Sri Lanka
- **Southeast Asia:** `sg` Singapore, `my` Malaysia, `id` Indonesia, `ph` Philippines, `th` Thailand, `vn` Vietnam
- **East Asia:** `jp` Japan, `cn` China, `kr` South Korea, `hk` Hong Kong
- **Europe:** `eu` (common EU rules), `mt` Malta, `gb` United Kingdom
- **Other:** `us` United States, `au` Australia

Each profile has a "Last checked" date and "Confidence notes". If a profile is more than 6 months old, or the user's question touches something listed as unverified, tell the user and suggest they confirm it with the official source named in the profile.

## Pick the module

| The user wants to... | Read |
|---|---|
| file / check supplier invoices, bills, receipts, expense claims | `modules/1-purchases.md` |
| create a sales invoice, quote-to-invoice, credit note | `modules/2-sales.md` |
| see who owes money, chase unpaid invoices, record payments received | `modules/3-receivables.md` |
| match a bank or card statement, find missing receipts | `modules/4-bank-reconciliation.md` |
| close the month, prepare the pack for the accountant, VAT/GST summary | `modules/5-month-end-pack.md` |

A request can need more than one module (e.g. "do this month's books" = 1, 4, then 5). Run them in that order.

## How to talk to the user

- Short sentences, plain words. The user is not an accountant.
- One preview table per step, then a clear question: "Approve all, some (give row numbers), or change something?"
- Put problems first, sorted by money at risk.
- Amounts with currency code and two decimals: `EUR 1,234.50`. Dates as `14 Nov 2026`.
- When finished, report what changed and where, in two or three lines.
