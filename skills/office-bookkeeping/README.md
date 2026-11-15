# Office Bookkeeping (Claude skill)

**Safe, worldwide bookkeeping help for small offices, run by non-accountants.**

One skill, five modules:

| Module | What it does |
|---|---|
| 1. Purchases | Reads supplier invoices and receipts (net, tax and gross per rate, tax IDs, currency) and checks the arithmetic and required fields. Catches duplicates even when the files differ, flags changed bank details as possible fraud, and files renamed copies. |
| 2. Sales | Issues invoices and credit notes with every required field, numbered in order with no gaps, and the correct tax wording. |
| 3. Receivables | Applies payments received (including part payments, bank fees and withholding tax), lists who owes what and for how long, and drafts reminders for you to send. |
| 4. Bank reconciliation | First checks that the statement adds up, then matches every line to a document, lists missing receipts and closes the month to a zero difference. |
| 5. Month-end pack | Builds a tidy folder for your accountant: registers, tax summary per rate, missing documents and numbered questions. |

## See it in action

**[Sample run (UAE)](examples/sample-run-uae.md)**: five fake supplier documents go in. One is a duplicate photo, one has changed bank details, one doesn't add up, one is missing the buyer's TRN and one is just a quotation. See exactly what the skill flags, what it asks, and what it writes after approval.

**[Test set](tests/README.md)**: 12 fake documents from 6 countries, each with its correct answer written down in advance, plus a script that scores the skill. Run it after any change.

## Why it's different

Built after reviewing the existing bookkeeping skills and their weak spots:

- **Never invents a figure.** Every number points back to the document and line it came from. Fields it can't read are marked, not guessed.
- **Preview, approve, then apply.** Nothing changes until you say yes. It never pays, sends or deletes anything.
- **Change log.** Every change is recorded, and your original files are never touched.
- **Finds real duplicates**, not just identical files: the same supplier and invoice number, or the same amount within 7 days.
- **Fraud check** on changed bank details: *verify by phone on a known number*.
- **Works one month at a time**, so errors don't build up month after month.
- **No accounting software needed.** It uses plain folders and spreadsheets.
- **Never fakes e-invoices.** It won't create QR codes, IRNs, UUIDs or clearance numbers. Where your country requires government e-invoicing, it tells you to issue through your certified system.

## Countries covered (27 profiles)

- **Middle East:** UAE, Saudi Arabia, Bahrain, Oman, Qatar, Kuwait, Egypt
- **South Asia:** India, Pakistan, Bangladesh, Sri Lanka
- **Southeast Asia:** Singapore, Malaysia, Indonesia, Philippines, Thailand, Vietnam
- **East Asia:** Japan, China, South Korea, Hong Kong
- **Europe:** EU common rules, Malta, United Kingdom
- **Other:** United States, Australia
- **Anywhere else:** a basic generic profile

Each profile lists the tax rates, tax-ID formats, required invoice fields, credit-note rules, e-invoicing status, record retention, concrete checks, sources, and a **Confidence notes** section saying what couldn't be verified.

## Important

This is **not tax advice**. Tax rules change often. Profiles were last checked in November 2026 and some details come from secondary sources (see each file's Confidence notes). When the tax treatment is unclear, the skill marks it `ASK ACCOUNTANT` instead of guessing.

## Install

- **Claude.ai / desktop app:** zip the `office-bookkeeping` folder and upload it under Settings → Capabilities → Skills.
- **Claude Code:** copy the folder into `~/.claude/skills/`.

On first use, it asks a few setup questions (country, tax registration, currency, folders) and creates your `books/` folder.

## Contribute a country

Copy `countries/_TEMPLATE.md`, fill it in from official sources, and open a pull request. Corrections to existing profiles are very welcome, especially from accountants in the country concerned.
