# Contributing your skill

Thanks for helping. This collection is for office workers, not programmers, so a skill you use at your desk every day is exactly what we want. You don't need to write code.

## What makes a good skill here

- **It solves a real, repeated office job:** invoices, rosters, reports, booking emails, stock lists, HR paperwork.
- **It works for other businesses**, not just yours. Put anything specific to your business in a **Your setup** block with `<PLACEHOLDERS>`.
- **It follows the [five rules](README.md#the-rules-every-skill-follows):** you approve, Claude applies; never guess; keep history; leave a trail; print-friendly.
- **It uses fake sample data only.** Never real customer names, phone numbers, emails, addresses or company records.

## How to add one (no coding needed)

1. **Fork** this repo: click **Fork** at the top right of the page.
2. In your fork, create a folder `skills/<your-skill-name>/`. Use lowercase words joined by hyphens.
3. Add a `SKILL.md` file there. Copy the shape of an existing one, for example [monthly-summary-report](skills/monthly-summary-report/SKILL.md):
   - frontmatter with `name` (same as the folder) and `description` (starting "Use when…" and listing the words people actually say)
   - a **Your setup (edit this once)** block
   - numbered **Steps**, ending with a check and a one-line report
4. Optional: add an `examples/` folder with small fake sample files.
5. Add one row for your skill to the table in `README.md`.
6. Click **Contribute → Open pull request**, and fill in the checklist.

You can do all of this in the GitHub website with the **Add file** button. You don't need git.

## Other ways to help

- Pick an issue labelled **good first issue** and build that skill.
- Add a country profile to [office-bookkeeping](skills/office-bookkeeping/countries/_TEMPLATE.md).
- Fix a typo, a broken link or an unclear step.
- Open an issue describing a job you'd like a skill for.

## Review

Every pull request is read and tested before it's merged, usually within a few days. Small changes may be suggested. That's normal and not a rejection.
