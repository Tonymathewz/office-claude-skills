# Office Claude Skills

**Claude skills for people who run offices, not code.**

These are Claude Agent Skills (SKILL.md files) that work in Claude.ai, the Claude desktop app and Claude Code.

Most skill collections on GitHub are written for programmers. This one is for the admin clerk, the dispatcher, the office coordinator: people who live in email, spreadsheets and Word documents and want Claude to take the repetitive work off their desk without ever acting behind their back.

Every skill here comes from real daily work in a busy transport office and has been stripped down to a general version you can adapt to your own business.

## The skills

| Skill | What it does |
|---|---|
| [email-approval-queue](skills/email-approval-queue/SKILL.md) | Reads incoming booking or change emails, turns each into a proposed change, shows you a preview, and applies nothing until you say yes. |
| [notice-to-route-mapper](skills/notice-to-route-mapper/SKILL.md) | Turns "closed on Friday" / "early finish on the 12th" notices into a list of the routes, jobs or shifts they affect, kept in an append-only calendar. |
| [monthly-summary-report](skills/monthly-summary-report/SKILL.md) | Builds a clean, printable month-end summary (Word or PDF) from a list of jobs, filed into the right month folder. |
| [office-bookkeeping](skills/office-bookkeeping/README.md) | **New.** Worldwide bookkeeping for non-accountants: supplier invoices, sales invoices and credit notes, chasing payments, bank reconciliation and the month-end pack for your accountant. 27 country profiles with extra depth for the Middle East and Asia. |
| [build-coach](skills/build-coach/SKILL.md) | **New.** Builds any project or office automation with you one step at a time from a saved plan, and checks each step before moving on. |
| [business-advisor](skills/business-advisor/SKILL.md) | **New.** Practical frameworks for pricing, launching, local marketing, social content, sales follow-up and "is this worth building?" |
| [improve-system](skills/improve-system/SKILL.md) | **New.** A weekly review of your Claude setup: finds overlapping or outdated skills and repeated corrections, and recaps your week. |

More are coming. See [Ideas](#ideas-for-future-skills), or [add your own](CONTRIBUTING.md).

## The rules every skill follows

1. **You approve, Claude applies.** Nothing is changed, sent or deleted without a preview and your yes.
2. **Never guess.** If something isn't in your map or your data, Claude asks instead of inventing a route number, a date or a customer.
3. **Keep history.** New information is added below old information. Nothing is silently overwritten.
4. **Leave a trail.** Every change carries a short note: what changed, why, the date of the email, and who sent it.
5. **Print-friendly by default.** Documents are designed to print well in black and white with minimal ink.

## How to install

**Claude.ai / Claude desktop app**
1. Download the skill folder you want (for example `skills/email-approval-queue`).
2. Zip the folder.
3. In Claude, go to **Settings → Capabilities → Skills** and upload the zip.

**Claude Code**
Copy the skill folder into `~/.claude/skills/` (for all projects) or `.claude/skills/` inside a project.

Then edit the **"Your setup"** section at the top of each `SKILL.md`. That is where your folder names, file names and business rules go.

## Make it yours

Each skill has a **Your setup** block with placeholders like `<YOUR CALENDAR FILE>`. Fill them in once and the rest of the skill works as written. The `examples/` folders contain small, fake sample files so you can see the expected format.

## Ideas for future skills

- Subcontractor job sheet with a map link for every stop
- Weekly roster / duty sheet builder
- "Compare the new version of this spreadsheet with the old one" checker

## Contributing

**Have a skill you use at your desk every day? Add it here.** You don't need to code: the whole process works in the GitHub website. See [CONTRIBUTING.md](CONTRIBUTING.md) for the steps and the checklist, or pick an issue labelled [good first issue](https://github.com/Tonymathewz/office-claude-skills/labels/good%20first%20issue).

Please use fake sample data only, never real customer names, phone numbers or company records.

## License

MIT. Use it, change it, share it.

Made by [Tony Mathew](https://github.com/Tonymathewz).
