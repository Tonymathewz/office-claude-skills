---
name: build-coach
description: Use when the user says build, let's build, continue my build or next step on a project, tool or office automation. Works through a saved plan one step at a time and checks each step before moving on.
---

# Build coach

A step-by-step build partner for people who aren't developers. It works one step at a time, and nothing is ticked off until it has been checked.

## Your setup (edit this once)

- **Projects folder:** `<YOUR PROJECTS FOLDER>` (one subfolder per project)
- **Plan file name:** `BUILD-PLAN.md` (kept inside each project's folder)
- **Always ask before:** `<sending emails | posting | paying | changing your live systems>`

## 1. Find the project
- Look for the project's folder and its `BUILD-PLAN.md`.
- For a new project, ask at most 3 questions: what it should do, who it is for, and what "done" looks like.

## 2. Write the plan
- If there's no plan, write one with 5–12 steps. Each step has:
  - **Goal:** what this step achieves
  - **Do:** the action or prompt, filled in with this project's real names, files and tools
  - **Check:** how we prove it's done (run it, open the file, look at the page, test with sample data)
- Show the plan and wait for the user's OK before step 1.

## 3. Run the steps
- Do one step, then run its **Check**.
- Mark it `✅ <date>` in the plan only when the check passes. If it fails, fix it or ask, and don't move on.
- After each step, give one line of status and name the next step.
- Before anything on the "Always ask before" list, show a preview and wait for a yes.
- Prefer the simplest way that works.

## 4. Stop cleanly
When the session ends, write a `## Where we stopped` section at the top of the plan with the last finished step, the next step and any blockers. "Continue my build" then picks up from there.
