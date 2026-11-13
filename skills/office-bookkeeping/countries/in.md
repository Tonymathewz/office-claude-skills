# India (IN) — invoice & bookkeeping profile

> Last checked: 2026-11-13. Rules change often. Not tax advice: confirm anything important with a local accountant (CA) or the GST portal.

## At a glance
| Item | Value |
|---|---|
| Tax name | Goods and Services Tax (GST): CGST (Centre) + SGST (State) or UTGST (Union Territory) for intra-state supplies; IGST for inter-state supplies, imports, exports and SEZ supplies |
| Tax authority | GSTN / GST portal (gst.gov.in), CBIC (cbic-gst.gov.in), state GST departments. E-invoice portal (IRP): einvoice1.gst.gov.in. E-way bill portal: ewaybillgst.gov.in |
| Rates | Since 22 Sep 2025 ("GST 2.0"): **5%** (merit), **18%** (standard), **40%** (demerit/luxury/sin, e.g. tobacco, pan masala, online gaming). Special rates for a few goods (e.g. 3% gold/silver, 0.25% rough diamonds, 1.5% cut diamonds). Nil/exempt items. Exports and SEZ supplies are zero-rated. The old **12% and 28% slabs are gone**. The GST compensation cess has ended (most goods from 22 Sep 2025; tobacco from 1 Feb 2026, replaced by central excise and a health/national-security cess outside GST) |
| Registration threshold | Aggregate turnover above ₹40 lakh (goods only, most states) / ₹20 lakh (services or mixed); ₹20 lakh / ₹10 lakh in special-category states. Mandatory regardless of turnover for inter-state suppliers of goods, e-commerce sellers, RCM-liable persons, etc. |
| Currency | INR. Export invoices may be in foreign currency, but the taxable value and GST must be computed in INR |
| Tax ID name & format | GSTIN, 15 characters: 2-digit state code + 10-char PAN + entity number (1–9, A–Z) + `Z` (default) + check character. Regex: `^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][1-9A-Z]Z[0-9A-Z]$` (normal taxpayers; UIN, TDS/TCS, NRTP and OIDAR IDs use other patterns) |
| Online tax-ID check | GST portal → Search Taxpayer → Search by GSTIN/UIN (on gst.gov.in). Shows legal name, status (Active/Cancelled), registration type (Regular/Composition) |
| Filing frequency & deadline | GSTR-1 (sales) by 11th of next month (or quarterly under QRMP with optional IFF by 13th); GSTR-3B (summary + payment) by 20th (QRMP: 22nd/24th after quarter); GSTR-9 annual by 31 Dec after FY. FY = 1 Apr–31 Mar |
| Record retention | 72 months from the due date of the annual return for that year (s.36 CGST Act); longer if an appeal/investigation is pending (until 1 year after final disposal) |

**State codes (first 2 digits of GSTIN):** 01 J&K, 02 HP, 03 Punjab, 04 Chandigarh*, 05 Uttarakhand, 06 Haryana, 07 Delhi, 08 Rajasthan, 09 UP, 10 Bihar, 11 Sikkim, 12 Arunachal, 13 Nagaland, 14 Manipur, 15 Mizoram, 16 Tripura, 17 Meghalaya, 18 Assam, 19 West Bengal, 20 Jharkhand, 21 Odisha, 22 Chhattisgarh, 23 MP, 24 Gujarat, 26 Dadra & Nagar Haveli and Daman & Diu* (25 = legacy Daman & Diu), 27 Maharashtra, 29 Karnataka, 30 Goa, 31 Lakshadweep*, 32 Kerala, 33 Tamil Nadu, 34 Puducherry, 35 Andaman & Nicobar*, 36 Telangana, 37 Andhra Pradesh (28 = old AP), 38 Ladakh*, 97 Other Territory, 99 Centre Jurisdiction. *UTGST (not SGST) applies in these UTs without a legislature.

## Full tax invoice: required fields
Rule 46 CGST Rules (tax invoice under s.31):
1. Supplier name, address, **GSTIN**.
2. Invoice number: consecutive, **max 16 characters**, only letters, digits, hyphen `-` and slash `/`, **unique within the financial year**. (Often missed: series longer than 16 chars, or reused across years without an FY marker.)
3. Date of issue.
4. Recipient name, address and GSTIN/UIN if registered.
5. Unregistered recipient, value **≥ ₹50,000**: name, address, delivery address, **state name and code** (below ₹50,000 only if the buyer asks).
6. HSN (goods) / SAC (services) code: **≥4 digits if prior-year aggregate turnover ≤ ₹5 crore (mandatory on B2B, optional on B2C); ≥6 digits if > ₹5 crore (all invoices)**.
7. Description; quantity and unit (UQC) for goods.
8. Total value; taxable value after discounts.
9. Rate and amount of tax, shown separately as CGST + SGST/UTGST or IGST (and cess if any).
10. **Place of supply with state name** (required for inter-state supplies; good practice always).
11. Delivery address if different from place of supply.
12. **Whether tax is payable on reverse charge** (Yes/No). Often missed.
13. Signature or digital signature (not needed for electronic invoices under the IT Act).
14. For e-invoicing taxpayers: **IRN and signed QR code** from the IRP (rule 46(r)).
15. Exports/SEZ: the endorsement "SUPPLY MEANT FOR EXPORT/SUPPLY TO SEZ UNIT OR SEZ DEVELOPER FOR AUTHORISED OPERATIONS ON PAYMENT OF INTEGRATED TAX" or "...UNDER BOND OR LETTER OF UNDERTAKING WITHOUT PAYMENT OF INTEGRATED TAX".

**Timing:** goods, at or before removal/delivery; services, within 30 days of supply (45 days for banks/insurers).

## Simplified invoice / receipt
- **Bill of supply** (rule 49): issued instead of a tax invoice for exempt/nil-rated supplies and by **composition** taxpayers. No GST is charged on it. Composition dealers must print "composition taxable person, not eligible to collect tax on supplies". The buyer **cannot claim ITC** on it.
- Supplies under ₹200 to an unregistered buyer who doesn't want an invoice: one consolidated invoice per day is allowed.
- Other documents: receipt voucher (advances), refund voucher, payment voucher + **self-invoice** for reverse-charge purchases from unregistered suppliers, delivery challan (rule 55) for movement without sale.
- B2C invoices by very large taxpayers (AATO > ₹500 crore) need a dynamic (payment) QR code.

## Credit and debit notes
- Issued under s.34 when the taxable value or tax charged was wrong, or goods were returned or services fell short. They must reference the original invoice(s) (rule 53: supplier GSTIN, nature of document, serial number of max 16 chars, date, recipient details, original invoice number/date, taxable value, rate, tax amount, signature).
- **Credit note time limit:** declare it in the return by **30 Nov after the end of the FY** of the original supply, or by the annual return date, whichever is earlier. No time limit for debit notes. ITC on a debit note follows the debit note's own date.
- Credit notes that reduce output tax require the buyer to reverse the matching ITC. Since GST 2.0 the old requirement for a pre-agreed discount linked to invoices has been removed (confirm current wording with accountant).
- E-invoicing taxpayers must also report credit/debit notes to the IRP (with an IRN). "Financial" or commercial credit notes without GST are outside e-invoicing.

## E-invoicing / clearance status (as of last-checked date)
- **System:** IRP (Invoice Registration Portal), e.g. einvoice1.gst.gov.in, plus private IRPs. The supplier uploads JSON (schema INV-01). The IRP validates it and returns an **IRN** (64-char hash), **Ack No. & Ack Date**, and a **digitally signed QR code**. Data flows to GSTR-1 and the e-way bill.
- **Scope:** any GSTIN whose PAN-level aggregate turnover exceeded **₹5 crore in any FY since 2017-18** (from 1 Aug 2023). Covers B2B, exports, SEZ, and B2B credit/debit notes. **Not** B2C.
- **Exempt entities:** banks/insurers/NBFCs, GTAs, passenger transport, multiplex cinema admissions, SEZ units, government departments/local authorities, OIDAR. Exempt documents: bills of supply, delivery challans, ISD invoices, imports/bills of entry.
- **30-day reporting limit:** taxpayers with **AATO ≥ ₹10 crore** cannot report a document to the IRP more than 30 days after its date (from 1 Apr 2025). Between ₹5 crore and ₹10 crore there's no hard block yet.
- **Corrections:** an IRN can be cancelled only within 24 hours (whole document). After that, issue a credit/debit note. You cannot reuse the same document number in the same FY.
- **From 1 Aug 2026:** when an e-way bill is made from an IRN for bill-to/ship-to, the **ship-to GSTIN** (or "URP" if unregistered) is mandatory. Voluntary e-way bill closure was also introduced.
- **Pending (not law yet):** the 57th GST Council (8 Oct 2026) recommended extending e-invoicing (AATO ≥ ₹5 crore) to RCM purchases from unregistered persons and to imports of services. Wait for the CBIC notification.
- **E-way bill basics:** needed before moving goods worth more than ₹50,000 per consignment (some intra-state limits differ). Part A has invoice/GSTIN/HSN data and Part B has the vehicle. Validity is 1 day per 200 km (20 km for over-dimensional cargo). From 1 Jan 2025 it can only be generated for documents ≤180 days old, and extensions are capped at 360 days.
- **The skill must NEVER generate, guess or "fill in" an IRN, Ack No., signed QR code or e-way bill number.** These only come from the IRP/EWB portal. If they're missing on an invoice that needs them, report it as a missing item. Drafts the skill prepares must be labelled "DRAFT — not registered on IRP".

## Numbering & language
- Max 16 characters, `[A-Za-z0-9/-]` only, unique per FY (Apr–Mar). Multiple series are allowed (e.g. per branch: `MUM/25-26/0001`). Separate series are recommended for credit notes, debit notes and bills of supply.
- Each GSTIN (state registration) has its own series.
- English is accepted everywhere; no mandatory language.

## Reverse charge, imports & cross-border
- **Place of supply decides the tax type:** if the supplier's state = place of supply → CGST + SGST/UTGST (equal halves); otherwise → IGST. Supplies to SEZ are always IGST (zero-rated). Since GST 2.0, the place of supply for **intermediary services** is the recipient's location.
- **Reverse charge (RCM):** the invoice must say "Tax payable on reverse charge: Yes". The buyer pays the GST in GSTR-3B and can claim ITC if eligible. Common cases: GTA (when not opting to charge), advocate services, security services, sponsorship, director fees, commercial property rented from an unregistered person. For purchases from unregistered suppliers under RCM, the buyer issues a self-invoice within 30 days.
- **Import of services:** IGST under RCM by the recipient. **Import of goods:** IGST collected by customs on the bill of entry (this is the ITC document).
- **Exports:** zero-rated, either with IGST paid and refunded, or under LUT without tax (the endorsement wording is required).

## Checks the skill must run for this country
- GSTIN matches `^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][1-9A-Z]Z[0-9A-Z]$`, and the state code is in the list above. Validate the check character (mod-36 Luhn-style; see Confidence notes). If it fails, flag it rather than reject.
- Characters 3–12 of the GSTIN form a valid PAN pattern `[A-Z]{5}[0-9]{4}[A-Z]`. For both parties, the 4th PAN character signals entity type (P = individual, C = company, F = firm, etc.).
- The supplier GSTIN's state code matches the state in the supplier's address.
- **Tax-type consistency:** if supplier state code == place-of-supply state code → CGST and SGST/UTGST present, equal, each = rate/2, and **no IGST**. Otherwise → **only IGST** at the full rate. SEZ/export → IGST or LUT endorsement. UTGST (not SGST) when the place of supply is 04/26/31/35/38.
- Rate is one of {0, 0.25, 1.5, 3, 5, 18, 40}. Flag 12% or 28% on invoices dated on/after 22 Sep 2025 as **probably outdated** (check that the item isn't a legacy or transition case). Flag any compensation cess on invoices dated after Feb 2026.
- Arithmetic: tax = taxable value × rate (±₹1 rounding per line); total = taxable + taxes (+ round-off line ≤ ₹1).
- Invoice number ≤16 chars, `[A-Za-z0-9/-]` only, and no duplicate within the same supplier GSTIN + FY.
- HSN/SAC present: ≥6 digits if the supplier's turnover is > ₹5 crore (or unknown and IRN present), else ≥4 digits on B2B. SAC codes start with `99`.
- B2B invoice shows the buyer GSTIN. B2C ≥ ₹50,000 shows the buyer name, address and state.
- The reverse-charge Yes/No indicator is present.
- If an IRN is present: it is 64 hex chars, and a QR code, Ack No. and Ack Date are present. If the buyer is B2B and the supplier is known/likely to have AATO > ₹5 crore (e.g. a large company, or IRNs on its other invoices), a missing IRN → **flag: invoice may be invalid for ITC**.
- If the supplier's AATO is ≥ ₹10 crore: Ack Date − invoice date ≤ 30 days.
- Supplier GSTIN status is Active and the type is Regular. If it's Composition, the invoice must be a bill of supply with no GST charged. (The user checks this on the portal; the skill does not claim it has verified it.)
- **ITC readiness (purchases):** the invoice appears in GSTR-2B / IMS for the period; it isn't a blocked credit under s.17(5) (e.g. food and beverages, personal motor vehicles, club memberships); the supplier is paid within 180 days of the invoice date; and ITC is claimed by 30 Nov after FY end.
- Credit/debit note references the original invoice number and date; a credit note is dated/declared by 30 Nov after the original FY.
- Goods movement > ₹50,000: an e-way bill number is recorded (12 digits). The skill never invents one.
- Export/SEZ invoice carries the required endorsement; a foreign-currency invoice shows the INR taxable value.

## Common mistakes
- Charging CGST+SGST on an inter-state sale (or IGST on an intra-state one). The tax paid under the wrong head isn't simply transferable.
- Using pre-22 Sep 2025 rates (12%/28%) from old item masters.
- Invoice numbers longer than 16 chars or restarting at 1 without an FY marker → duplicates.
- Missing the buyer GSTIN or the wrong state code → buyer loses ITC.
- Booking ITC for invoices not in GSTR-2B, or not paying suppliers within 180 days.
- E-invoice-liable supplier issuing a paper invoice without an IRN (invalid invoice).
- Wrong place of supply on services (e.g. hotel or event services follow the property/event location).

## Sources
- https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter6/rule46_v1.00.html (Rule 46 text, CBIC)
- https://pib.gov.in/PressReleasePage.aspx?PRID=1708713 (HSN digits by turnover from 1 Apr 2021)
- https://gstcouncil.gov.in/sites/default/files/2024-02/pib1865179.pdf (30 Nov limit for credit notes and ITC)
- https://cleartax.in/s/next-generation-gst-reforms (GST 2.0 slabs)
- https://www.ey.com/en_in/technical/alerts-hub/2025/09/gst-council-announces-major-rate-rationalization-and-trade-facilitation-measures
- https://www.businesstoday.in/personal-finance/tax/story/tobacco-tax-regime-from-february-1-excise-duty-health-cess-replace-gst-compensation-levy-513811-2026-01-31
- https://tallysolutions.com/business-guides/what-changed-in-e-invoicing-compliance-in-2026/
- https://tallysolutions.com/gst/e-invoicing-threshold/
- https://www.mahagst.gov.in/public/uploads/gstnadvisory/1760531580_293%20Advisory%20Time%20Limit%20for%20Reporting%20e%20Invoice%20on%20the%20IRP%20Portal%20%20Lowering%20of%20Threshold%20to%20AATO%2010%20Crores%20and%20Above.pdf (GSTN advisory, seen in search results only; could not be fetched)
- https://taxo.online/latest-news/gstn-system-enhancements-new-e-invoice-and-e-way-bill-api-changes-effective-1-august-2026/
- https://lookuptax.com/tax-changes/india/gst-council-57-einvoicing-extension
- https://www.drishtiias.com/daily-updates/daily-news-analysis/57th-gst-council-meeting
- https://busy.in/gst/gst-section-16-4-itc-time-limit-2026/
- https://www.knowyourgst.com/gstlaw/cgst-act/36-period-of-retention-of-accounts-36/
- https://cleartax.in/s/time-limit-for-e-way-bill-generation

## Confidence notes
- The official portals (gst.gov.in, einvoice1.gst.gov.in, cbic-gst.gov.in) could not be fetched in this session. E-invoice, IRP and 30-day-rule facts come from the CBIC rule text plus secondary sources and a GSTN advisory title.
- **Special rates** (3%, 0.25%, 1.5%) and their survival after GST 2.0 are not confirmed from an official rate notification. The 5/18/40 structure is confirmed by several sources.
- The **GSTIN check-character algorithm** (mod-36, weights alternating 1 and 2, sum of quotient + remainder) is the widely used community implementation, not an officially published spec. Treat a failure as a warning.
- Registration thresholds, return due dates, the ₹200 consolidated-invoice rule, the B2C dynamic QR (> ₹500 crore), RCM service list, the 180-day payment rule and the IMS/GSTR-2B mechanics are well established but were not re-verified against official text in this session.
- 57th GST Council recommendations (Oct 2026) are **not yet notified**. Most are expected from 1 Apr 2027. Recheck before relying on them.
- Whether the 30-day IRP limit applies to credit/debit notes as well as invoices: believed yes, not verified from the advisory text.
