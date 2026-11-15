# Sample run: a month of supplier invoices (UAE)

This shows what a run of **Module 1 (Purchases)** looks like for a small UAE office. **Every company, number and TRN below is made up.**

## The setup

`books/setup.md` (created on first run):

```
Legal name:            Example Logistics LLC
Country:               ae
Tax registration type: VAT registered
Tax ID (TRN):          100123456700003
Base currency:         AED
Documents arrive in:   Inbox/
Approves payments:     Office manager
```

`Inbox/` contains five files the office received in November:

| File | What it is |
|---|---|
| `scan_0041.pdf` | Tax invoice from Gulf Office Supplies LLC |
| `Desert Fleet inv 457.pdf` | Tax invoice from Desert Fleet Services (emailed) |
| `IMG_2210.jpg` | Phone photo of the **same** Desert Fleet invoice (from the driver) |
| `fuel receipt nov.pdf` | Receipt from Al Noor Fuel Trading |
| `quotation_tyres.pdf` | A quotation from a tyre shop |

Plus an email from "Gulf Office Supplies" saying *"Please note our new bank account for all future payments"*.

## What the user says

> Process this month's supplier invoices.

## What the skill shows (the preview)

Problems first, sorted by money at risk. Nothing has been changed yet.

| # | File | Supplier | Inv no. | Date | Cur | Net | VAT | Gross | Claimable? | Flags | New file name |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Desert Fleet inv 457.pdf | Desert Fleet Services | INV-0457 | 04 Nov 2026 | AED | 12,000.00 | 600.00 | 12,600.00 | **NO** (buyer TRN missing) | Over AED 10,000 without our TRN | 2026-11-04 Desert Fleet Services INV-0457 12600.00-AED.pdf |
| 2 | IMG_2210.jpg | Desert Fleet Services | INV-457 | 04 Nov 2026 | AED | 12,000.00 | 600.00 | 12,600.00 | n/a | **POSSIBLE DUPLICATE of row 1** | not filed |
| 3 | scan_0041.pdf | Gulf Office Supplies LLC | GOS-2201 | 02 Nov 2026 | AED | 2,000.00 | 100.00 | 2,100.00 | YES | **BANK DETAILS CHANGED: VERIFY BY PHONE ON A KNOWN NUMBER BEFORE PAYING** | 2026-11-02 Gulf Office Supplies GOS-2201 2100.00-AED.pdf |
| 4 | fuel receipt nov.pdf | Al Noor Fuel Trading | R-88412 | 09 Nov 2026 | AED | 800.00 | 40.00 | 850.00 | CHECK | **Totals don't add up** (800.00 + 40.00 = 840.00, receipt says 850.00) | 2026-11-09 Al Noor Fuel Trading R-88412 850.00-AED.pdf |
| 5 | quotation_tyres.pdf | Example Tyres | Q-301 | 10 Nov 2026 | AED | 3,400.00 | 170.00 | 3,570.00 | n/a | **Quotation, not an invoice** | moved to `review/` list |

**What the flags mean, in plain words:**

1. **Desert Fleet INV-0457**: The invoice is over AED 10,000, but it doesn't show *our* name and TRN. Under the UAE profile, that means the AED 600 VAT may not be claimable. **Suggested action:** ask Desert Fleet to reissue it with "Example Logistics LLC, TRN 100123456700003". You can still record it and pay it.
2. **IMG_2210.jpg**: Same supplier, same amount, same date, and the invoice number matches once the leading zero is ignored (INV-457 = INV-0457). It looks like the driver's photo of the emailed invoice. **Suggested action:** don't record it twice. Keep the PDF (row 1) and note the photo as a duplicate.
3. **Gulf Office Supplies GOS-2201**: The invoice itself is fine, but an email asks you to pay a *new* bank account. Invoice fraud usually starts exactly like this. **Suggested action:** call Gulf Office Supplies on the number in `suppliers.csv`, *not* the one in the email, and confirm the change before any payment. Until then, this invoice stays off the payment list.
4. **Al Noor Fuel R-88412**: Net + VAT = AED 840.00, but the total says AED 850.00. The receipt may include a non-VAT item (for example a car wash), or something was misread. **Suggested action:** check the paper receipt. I won't guess which figure is right.
5. **quotation_tyres.pdf**: A quotation isn't a tax invoice, so it's not recorded as a purchase. It goes on the review list.

*Each TRN was checked for format (15 digits, starting with 100). New suppliers: verify the TRN on EmaraTax and keep a dated screenshot. I haven't done that for you.*

> **Approve all, some (give row numbers), or change something?**

## What the user answers

> Approve 1 and 3. For 4, the receipt has a AED 10 car wash without VAT, so record it. Mark 2 as a duplicate. I'll call Gulf Office Supplies tomorrow.

## What the skill does (and only this)

**Files:** copies only. The originals in `Inbox/` are never moved or edited.

```
documents/2026-11/purchases/2026-11-04 Desert Fleet Services INV-0457 12600.00-AED.pdf
documents/2026-11/purchases/2026-11-02 Gulf Office Supplies GOS-2201 2100.00-AED.pdf
documents/2026-11/purchases/2026-11-09 Al Noor Fuel Trading R-88412 850.00-AED.pdf
```

**`purchases-register.csv`** gets three new rows (main columns shown):

| doc_id | status | supplier | invoice_no | gross_total | tax_by_rate | tax_claimable | flags |
|---|---|---|---|---|---|---|---|
| P-2026-11-001 | NEW | Desert Fleet Services | INV-0457 | 12,600.00 | 5%: 12,000.00 / 600.00 | NO - buyer TRN missing | Reissue requested? |
| P-2026-11-002 | NEW | Gulf Office Supplies LLC | GOS-2201 | 2,100.00 | 5%: 2,000.00 / 100.00 | YES | BANK DETAILS UNVERIFIED |
| P-2026-11-003 | NEW | Al Noor Fuel Trading | R-88412 | 850.00 | 5%: 800.00 / 40.00; out of scope: 10.00 | YES | Car wash AED 10.00 without VAT (confirmed by user) |

**`suppliers.csv`**: the new bank details for Gulf Office Supplies are added as a **new line marked `UNVERIFIED`**. The old details are kept.

**`change-log.csv`** (extract):

```
datetime,module,action,record,field,old_value,new_value,source_document,approved_by
2026-11-15 09:41,purchases,add,P-2026-11-001,,,"INV-0457 AED 12,600.00",Desert Fleet inv 457.pdf,user
2026-11-15 09:41,purchases,mark duplicate,IMG_2210.jpg,,,duplicate of P-2026-11-001,IMG_2210.jpg,user
2026-11-15 09:41,purchases,add,P-2026-11-003,gross,,"850.00 incl. 10.00 car wash without VAT",fuel receipt nov.pdf,user
2026-11-15 09:41,suppliers,add bank details,Gulf Office Supplies LLC,bank,****4471,"****9038 UNVERIFIED",email of 14 Nov,user
```
## Later: "Who do we need to pay this week?"

```
Ready to pay (approved, due by 21 Nov):
  Desert Fleet Services   INV-0457   AED 12,600.00   due 18 Nov

Held back:
  Gulf Office Supplies    GOS-2201   AED  2,100.00   BANK DETAILS UNVERIFIED - call first
```

The skill makes the list. **A person makes the payment.**

## What this run shows

- It reads **net, VAT and gross**, not just the total, and checks that they add up.
- It catches the **duplicate** even though one copy is a phone photo with a slightly different invoice number.
- It treats a **bank-detail change** as a fraud risk and keeps that invoice off the payment list until someone calls.
- It applies the **UAE rule** about buyer TRN on invoices over AED 10,000.
- It **never guesses** the fuel receipt. It asks, and records the user's answer.
- Nothing changes until the user approves, and every change is logged.
