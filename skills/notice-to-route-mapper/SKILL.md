---
name: notice-to-route-mapper
description: Use when the user shares a closure, early-finish, late-start or change-in-time notice (from a school, client site, venue or employer) and wants to know which routes, jobs or shifts it affects, or wants the notice added to their calendar file.
---

# Notice to route mapper

Turn notices like "School closed on Friday 12 December" or "Early dismissal at 11:30 on the 19th" into:
1. a row in an **append-only calendar**, and
2. a clear list of **which of your routes, jobs or shifts are affected**.

Works for school transport, contract cleaning, staff shuttles, catering, or any business whose work depends on another organisation's timetable.

## Your setup (edit this once)

- **Calendar file:** `<YOUR CALENDAR FILE>.csv` (format: `examples/calendar.csv`)
- **Route map file:** `<YOUR ROUTE MAP FILE>.csv` (format: `examples/route-map.csv`)
- **Where to file a copy of each notice:** `<YOUR NOTICES FOLDER>/<YEAR>/`
- **Date format used in notices:** `<DAY-FIRST (12/10 = 12 Oct) or MONTH-FIRST>`

## Golden rules

1. **Append only.** Never overwrite or delete an existing calendar row. If a new notice changes an earlier one, mark the old row's status as `SUPERSEDED` and add the new row below it. The last matching row wins.
2. **Never guess a mapping.** If a site is not in the route map, do not pick routes yourself. Show the user the likely candidates and let them decide, then add the confirmed mapping to the route map.
3. **One route, many sites is allowed.** A route that serves two sites is affected by notices from either one. Check both.
4. **"Ours or not" is decided by the route map, not by memory.** If a site seems unfamiliar, search the map before saying it isn't yours.
5. **Keep the evidence.** Save a dated copy of every notice (`YYYY-MM-DD <site>.md`) so anyone can check later.

## Steps

1. **Read the notice.** Pull out: site name, date(s), type (`CLOSED`, `EARLY FINISH`, `LATE START`, `OTHER`), new times, reason.
2. **Normalise the date** using the format in Your setup. If it's ambiguous (e.g. `05/06`), say which reading you used.
3. **Look up the site** in the route map.
   - Found: list its routes.
   - Not found: stop and ask (rule 2).
4. **Check for an earlier row** for the same site and date. If one exists, plan to supersede it (rule 1).
5. **Preview** before writing:

   | Date | Site | Type | New time | Routes affected | Replaces earlier row? |
   |---|---|---|---|---|---|

6. **After the user approves:** append the rows, update superseded rows, and file the notice copy.
7. **Summarise** in one or two lines, e.g. "3 routes affected on Fri 12 Dec: R12, R14 AM cancelled; R20 PM moved to 11:30."

## Weekly use

Ask: "What's changing next week?" Read the calendar for the next 7 days, take only the live (non-superseded) rows, and list them by day and route. This is a good thing to print and pin up for drivers or staff.
