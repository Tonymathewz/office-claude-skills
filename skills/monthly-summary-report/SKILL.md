---
name: monthly-summary-report
description: Use when the user asks for a month-end summary, monthly report or "summary for the boss" built from a list of trips, jobs, bookings or shifts. Produces a clean, printable Word or PDF document grouped by route or client and files it in the right month folder.
---

# Monthly summary report

Build the same professional month-end summary every month from a list of jobs, so the boss always gets a report that looks familiar and is easy to check.

## Your setup (edit this once)

- **Input:** `<YOUR JOB LIST>` (a spreadsheet or CSV; format: `examples/jobs.csv`)
- **Group by:** `<route | client | category>`
- **Logo:** `<PATH TO YOUR LOGO>` (optional)
- **Save to:** `<YOUR REPORTS FOLDER>/<YEAR>/<NN Month YYYY>/`
- **Output format:** `<Word (.docx) | PDF>`

## Layout rules

1. **Logo and title at the top:** `<Report name> · <Month YYYY>`
2. **One block per group** (route, client or category): name, then the dates it ran, then the count.
3. **No boxes or borders around blocks.** Use spacing and a bold heading instead. It prints cleaner.
4. **Give rows of dates room to breathe.** Don't pack them tightly.
5. **Black and white friendly.** Black text, thin lines, no colour fills, so it prints well on any office printer.
6. **Totals at the end:** jobs per group and the grand total.
7. **Carry-over days are named.** If the month's period includes days from the previous or next month (e.g. 30 September in the October report), say so in the heading and include them in the count.

## Steps

1. **Load** the job list for the month and check it: missing dates, duplicate rows, cancelled jobs that are still listed. Report problems before building.
2. **Group** the jobs and sort each group's dates in order.
3. **Show a quick preview** of the counts per group and the total. Ask the user to confirm before building the document.
4. **Build** the document following the layout rules.
5. **Save** it into the month subfolder. Never leave loose files in a folder root. Create the month folder if it doesn't exist.
6. **Check** by opening the result (or rendering it to an image) to confirm it fits the page and the totals match the preview.
7. **Report** the file name and where it was saved in one line.

## Tip

Once the first month looks right, keep that document as the reference. Each new month should match it exactly. Only the data changes.
