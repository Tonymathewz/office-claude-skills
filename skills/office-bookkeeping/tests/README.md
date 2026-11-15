# Test set for office-bookkeeping

12 fake supplier documents, each with its **correct answer written down in advance** (`expected.json`). Run the skill on them, save its answers, and `score.py` tells you which cases pass.

Use it to:
- check the skill still works after you edit it or a country profile
- compare Claude models, or Claude with and without the skill
- show others (and accountants) exactly what the skill is expected to catch

**Every company, tax ID and amount here is made up.**

## The cases

| Case | Country | What it tests | Expected result |
|---|---|---|---|
| T01 | UAE | Clean tax invoice | Claimable, **no** flags |
| T02 | UAE | Over AED 10,000 without our TRN | `BUYER_TAX_ID_MISSING`, not claimable |
| T03 | UAE | Same invoice already in the register (INV-457 vs INV-0457) | `POSSIBLE_DUPLICATE` |
| T04 | UAE | 800 + 40 ≠ 850 | `ARITHMETIC_MISMATCH` |
| T05 | UAE | "Please note our new bank account" | `BANK_DETAILS_CHANGED` |
| T06 | UAE | Pro-forma invoice | `NOT_AN_INVOICE` |
| T07 | Malta | Fiscal receipt for a business purchase | `NOT_TAX_INVOICE`, not claimable |
| T08 | India | Same-state supply charged IGST instead of CGST + SGST | `TAX_TYPE_MISMATCH` |
| T09 | Saudi Arabia | Simplified invoice for a B2B purchase, no QR code | `QR_MISSING`, `NOT_TAX_INVOICE` |
| T10 | Japan | Supplier has no T registration number | `NO_REGISTRATION_NUMBER`, partial (70%) credit |
| T11 | Malta + Germany | EU reverse charge | `REVERSE_CHARGE` |
| T12 | Malta | Decimal commas (`1.234,50`) and day-first date (`05/06/2026`) | Amounts read correctly, date = 5 June 2026, no flags |

Each case folder has:
- `setup.md`: the buyer's business (what `books/setup.md` would say)
- `document.txt`: the supplier document, as text
- `purchases-register.csv` / `suppliers.csv`: existing records, only where the case needs them
- `expected.json`: the correct answer

## Flag codes

The skill writes flags in plain words for people. For the test, Claude maps them to these codes:

| Code | Meaning |
|---|---|
| `ARITHMETIC_MISMATCH` | Lines, net, tax and total don't add up |
| `BUYER_TAX_ID_MISSING` | Our name or tax ID is missing where the country requires it |
| `POSSIBLE_DUPLICATE` | Looks like a document already recorded |
| `BANK_DETAILS_CHANGED` | Bank details differ from the ones on record |
| `NOT_AN_INVOICE` | Pro-forma, quotation or statement |
| `NOT_TAX_INVOICE` | A receipt or simplified invoice that can't support a tax claim |
| `TAX_TYPE_MISMATCH` | Wrong tax type for the place of supply (e.g. IGST vs CGST + SGST) |
| `QR_MISSING` | A required e-invoice QR code is missing |
| `NO_REGISTRATION_NUMBER` | Supplier registration number missing (e.g. Japan T-number) |
| `REVERSE_CHARGE` | Buyer must self-account the tax |
| `FX_MISSING` | Foreign currency without the required rate or local-currency tax |

## Document types

`tax_invoice` meets the country's tax-invoice rules (a normal EU VAT invoice with "Reverse charge" counts). `simplified_invoice` is the country's short form. `invoice` is a commercial invoice that is **not** a valid tax invoice (e.g. Japan without a T-number). Then `receipt`, `credit_note` and `proforma`.

## First blind run

**11 of 12 passed** (15 Nov 2026, Claude Opus 5.5). A fresh agent ran the skill on these cases without seeing the answers. Every flag, amount and tax decision was right. The one miss (T11) was the document type: it called a German reverse-charge invoice `invoice` instead of `tax_invoice`. That happened because the test didn't yet define document types. The definitions above were added after this run, along with matching wording in Module 1.

## How to run it

1. Give Claude the `office-bookkeeping` skill and this `tests` folder.
2. Paste this prompt:

```
Test mode for the office-bookkeeping skill. For each folder in tests/cases,
treat setup.md as books/setup.md and any CSV files as the existing books,
then run Module 1 (Purchases) checks on document.txt using the skill and the
right country profile. Do not ask questions and do not write any files except
the result. Save one JSON list to results.json, one object per case:
{"id": "T01", "doc_type": "tax_invoice|simplified_invoice|invoice|receipt|proforma|credit_note",
 "net": 0.00, "tax": 0.00, "gross": 0.00, "issue_date": "YYYY-MM-DD",
 "claimable": "YES|NO|CHECK|PARTIAL 70%|REVERSE CHARGE|ASK ACCOUNTANT|N/A",
 "flags": ["CODE", ...]}
Use only the flag codes listed in tests/README.md. Copy amounts as written on
the document; never correct them.
```

3. Score it:

```bash
python3 score.py results.json
```

You'll see `PASS` / `FAIL` per case with the reason, and a total like `11/12 cases passed`. Money is compared to the cent, and flags must be present (or absent) exactly as listed in `expected.json`.

## Adding a case

Copy a case folder, change the document and `expected.json`, and add a row to the table above. Please keep everything fictional. When a case covers a country rule, the expected answer must match what that country's profile says. If the profile is wrong, fix the profile in the same pull request.
