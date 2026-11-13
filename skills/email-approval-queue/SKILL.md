---
name: email-approval-queue
description: Use when the user asks to "process my email queue", "check the booking emails" or similar. Turns booking, change and cancellation emails into proposed changes, shows a preview, and applies them to the user's booking system or spreadsheet only after the user approves.
---

# Email approval queue

Turn a pile of booking emails into a clean list of proposed changes, then apply only the ones the user approves.

## Your setup (edit this once)

- **Where emails come from:** `<YOUR MAILBOX / EXPORT FOLDER>` (an email connector, a folder of saved .eml/.msg files, or a pasted list)
- **Where changes go:** `<YOUR BOOKING SYSTEM OR SPREADSHEET>`
- **Customers who also change bookings by phone:** `<LIST>`. For these, a difference between the email and the system is not automatically an error.
- **Your own business rules:** `<e.g. vehicle sizes, minimum notice, default pick-up buffer>`

## Golden rules

1. **Preview first, apply after yes.** Never change, send or delete anything before the user approves that exact item.
2. **Never invent.** No made-up job numbers, route codes, addresses, times or passenger counts. If it isn't in the email or the system, mark it **Needs info**.
3. **A cancellation must say so.** Only propose a cancellation when the email clearly says cancel / no longer needed / no transport. A vague email is never a cancellation.
4. **A question is not a change.** "Could you confirm whether…" or "Is it possible to…" goes under **Needs your reply**, not under changes.
5. **Read the whole thread.** Amendments often arrive as replies in old threads. The latest message in the thread wins, but show the user what it replaced.
6. **Read attachments.** Spreadsheets and PDFs attached to an email often hold the real details.
7. **Never send email for the user.** Draft replies are shown as text for the user to send themselves.

## Steps

1. **Collect** the new emails since the last run. Skip newsletters, auto-replies and anything already handled.
2. **Classify** each email as one of:
   - **New booking**
   - **Change** (time, date, place, passengers, vehicle)
   - **Cancellation** (explicit only, see rule 3)
   - **Needs your reply** (questions, unclear requests)
   - **Info only** (no action)
3. **Match** each change or cancellation to the existing booking: same customer, same date, same route or job. If two bookings could match, list both and ask.
4. **Check for problems** before proposing:
   - Double booking: the same job already exists
   - Date or time that doesn't make sense (a past date, a weekend for a weekday-only service, AM/PM mix-ups)
   - Arrival time given instead of pick-up time: suggest an earlier pick-up and say why
   - Passenger count bigger than the vehicle
5. **Show the preview** as one table:

   | # | Email (date, sender) | Type | Booking affected | Proposed change | Warnings |
   |---|---|---|---|---|---|

   Then list the **Needs your reply** emails separately with a suggested reply draft for each.
6. **Wait for approval.** The user may approve all, some ("1, 3, 4") or edit an item first.
7. **Apply** only the approved items. On every change add an office note:
   `Changed <what> per email of <date> from <sender>: <reason>`
8. **Report** what was applied, what was skipped and anything that failed. Keep it short.

## Output style

- Plain language, short lines, one table.
- Dates written out unambiguously (e.g. `Fri 14 Nov 2026`). Be careful with day-first vs month-first dates and say which you assumed.
