# Pakistan (PK) — invoice & bookkeeping profile

> Last checked: 2026-11-13. Rules change often. Not tax advice: confirm anything important with a local accountant or FBR.

## At a glance
| Item | Value |
|---|---|
| Tax name | Sales Tax on goods (federal, Sales Tax Act 1990). Sales tax on **services** is provincial: Sindh (SRB), Punjab (PRA), Khyber Pakhtunkhwa (KPRA), Balochistan (BRA); Islamabad Capital Territory services are federal (FBR) |
| Tax authority | Federal Board of Revenue (FBR), https://fbr.gov.pk. E-invoicing gateway run by PRAL |
| Rates | Goods: **18%** standard (s.3(1)). Reduced rates are set item by item in the Eighth Schedule (e.g. 1%, 7%, 10%). Zero-rated: Fifth Schedule (exports etc.). Exempt: Sixth Schedule. **Further tax 4%** on top for supplies to buyers who are unregistered or not on the Active Taxpayer List (s.3(1A)). Services (provincial): Sindh 15%, Punjab 16%, KP 15%, ICT 15%, Balochistan (check) |
| Registration threshold | No general turnover threshold for goods: registration depends on category (manufacturers, importers, wholesalers, retailers etc.). The cottage-industry exclusion is ≤ PKR 8 million turnover (plus conditions). Tier-1 retailer turnover threshold is PKR 200 million (from 1 Jul 2026) |
| Currency | PKR. Show tax in PKR |
| Tax ID name & format | **NTN** (National Tax Number): 7 digits (often shown with a check digit, `1234567-8`). Individuals use their 13-digit **CNIC** (`12345-1234567-1`). **STRN** (Sales Tax Registration Number): 13 digits (e.g. `00-00-0000-000-00`). Provincial services registrations have their own numbers (often NTN-based) |
| Online tax-ID check | FBR Active Taxpayer List (ATL) and registration inquiry on FBR's e-portal. POS/digital invoices can be checked with the FBR "Tax Asaan" app or SMS to 9966 |
| Filing frequency & deadline | Monthly. Sales annex (Annex-C) by the 10th, payment by the **15th**, e-return by the **18th** of the following month |
| Record retention | 6 years after the end of the tax period (s.24), longer if proceedings are pending. Electronic invoice records: 6 years (r.150S) |

## Full tax invoice: required fields
s.23(1) Sales Tax Act plus r.150R(13) Sales Tax Rules (digital invoices):
1. Supplier name, address, **NTN/STRN**.
2. Buyer name, address, **NTN/STRN**. For unregistered buyers, the buyer's **CNIC or NTN** (often missed).
3. Date of issue (and tax period).
4. Serial number.
5. Description, quantity, unit of measure, **HS code** (PCT), and the SRO/schedule reference where a reduced rate or exemption applies.
6. Value excluding tax.
7. Rate and amount of sales tax, plus further tax, extra tax, withholding and FED fields where relevant.
8. Value including tax.
9. **FBR invoice number** (returned by FBR's system) and a **verifiable QR code**.
10. Software/POS registration number and the **FBR Digital Invoicing logo**.
- Only one tax invoice per taxable supply. Since the Finance Act 2026, invoices are also required for **exempt** supplies.

## Simplified invoice / receipt
- Retailers selling to the general public issue POS receipts. **Tier-1 retailers** must be integrated with FBR POS: the receipt shows the FBR invoice number and QR code, and the shop must display the "Integrated with FBR" sign.
- Some invoice fields (further tax, extra tax, FED) don't apply to pure retailers selling to the public.
- Input tax can only be claimed on an invoice that has the buyer's registration details and a valid FBR invoice number. Retail receipts to the public don't support a claim.

## Credit and debit notes
- s.9: issued when a supply is cancelled, goods are returned, or the price changes. Both parties adjust input/output tax in the return for the period.
- They must reference the original invoice, be issued **electronically through the integrated system**, and be kept 6 years (r.150S(2)).
- Under e-invoicing, cancellations or changes are made via a debit/credit note. A 72-hour window to cancel/edit a digital invoice was reported (STGO 01 of 2026).
- Time limit: see Confidence notes (commonly cited as 180 days from the original supply).

## E-invoicing / clearance status (as of last-checked date)
- **System:** FBR Digital Invoicing (DI), a real-time JSON REST API via PRAL or another FBR-licensed integrator (PRAL integration is free). The invoice is posted before issue. FBR returns status "00" valid / "01" invalid plus the **FBR invoice number**. Not UBL/Peppol.
- **Legal basis:** Chapter XIV Sales Tax Rules (SRO 69(I)/2025). Schedule set by SRO 1852(I)/2025: **all categories had to be live by 31 Dec 2025**. It now applies to every sales-tax registered person (B2B, B2C, exempt and export sales in Annex-C). Extended to FED and ICT services by SRO 1666(I)/2026 (29 Sep 2026).
- **Offline invoices** (power/internet failure) must be marked as offline and uploaded within 24 hours of restoration.
- **Tier-1 retailer POS** integration has applied since 2019.
- **The skill must NEVER create, guess or alter an FBR invoice number or QR code**, or present a draft as a valid sales tax invoice. A draft without an FBR number is "DRAFT — not reported to FBR".

## Numbering & language
- Sequential serial numbers per business/POS. The FBR invoice number (format per rules `XXXXXX-DDMMYYHHMMSS-0001`; PRAL samples differ) is separate from your own number. Store both.
- Language: **Urdu or English**.

## Reverse charge, imports & cross-border
- Imports: sales tax (and value-added tax on commercial imports) is collected by Customs on the Goods Declaration. The GD is the input-tax document.
- Exports: zero-rated (Fifth Schedule). Exports must still be reported as digital invoices.
- Services: the provincial tax depends on where the service is rendered or where the recipient is (province rules). Some provinces apply reverse charge or withholding on specified services. Check the provincial law.
- Withholding: specified buyers (withholding agents) withhold part of the sales tax under the Eleventh Schedule and Withholding Rules. Record the withholding on the invoice/payment.

## Checks the skill must run for this country
- Supplier STRN is 13 digits after removing separators. NTN is 7 digits (+ optional check digit); a CNIC is 13 digits (`^\d{5}-?\d{7}-?\d$`).
- Buyer registration: if no STRN/NTN, or the buyer is not on the ATL → expect the 4% further tax line (goods), and the buyer's CNIC/NTN must be on the invoice.
- Rate is 18% for standard goods. Any other rate must cite an SRO/schedule reference. Services tax matches the province (15% Sindh/KP/ICT, 16% Punjab).
- Arithmetic: value excl. tax × rate = sales tax (±1 PKR); excl. + tax (+ further tax) = incl.
- HS code present on each line.
- **FBR invoice number and QR code present** on every sales tax invoice dated on/after the supplier's integration date (all registered persons by 31 Dec 2025). If missing, flag "input tax may be disallowed".
- Purchases: the supplier appears in the buyer's Annex-A / sales tax return auto-population. Flag invoices that are not reflected.
- Credit/debit note references the original invoice and FBR number.
- Invoice language is English or Urdu; amounts are in PKR.

## Common mistakes
- Claiming input tax on invoices from suppliers who are not active (not on the ATL) or without an FBR invoice number.
- Charging federal sales tax on services that are provincial (or the wrong province's rate).
- Forgetting the 4% further tax when selling to unregistered buyers.
- Issuing paper invoices after integration, or editing invoices instead of issuing debit/credit notes.

## Sources
- https://fbr.gov.pk/faqs/173967/173969 (FBR e-invoicing FAQs)
- https://download1.fbr.gov.pk/SROs/2025129141598258SRO69%28I%292025.pdf (SRO 69(I)/2025, Chapter XIV rules)
- https://fbr.gov.pk/Budget2026-27/SalientFeatures/Salient-Feature.pdf (Finance Bill 2026 salient features)
- https://download1.fbr.gov.pk/Docs/20267171373418951SalesTaxAct1990updatedupto30.06.2026.pdf (Sales Tax Act updated to 30.06.2026; seen in search, not read)
- https://lookuptax.com/docs/einvoicing/fbr-digital-invoicing-pakistan
- https://lookuptax.com/docs/country/pakistan-sales-tax-guidelines-indirect-tax

## Confidence notes
- The FBR FAQ page still shows the older SRO 709 dates (Jun/Jul 2025). The later schedule (SRO 1852(I)/2025, all categories by 31 Dec 2025) comes from a secondary source and was not read in the SRO itself.
- STRN format and the NTN check-digit rule: FBR publishes no check-digit algorithm. Only format checks are possible.
- The credit/debit note **time limit (180 days)**, the **input-tax claim window (within 6 succeeding tax periods)**, the s.8B input-adjustment cap (90% of output tax, now variable by government) and the banking-channel payment condition (s.73) were not verified in this session.
- Balochistan services rate and Punjab's 2026-27 rate are unconfirmed.
- The QR size (7×7 mm in the rules vs 1 inch in the PRAL API spec) and the FBR invoice number format conflict between FBR sources.
- STGO 01 of 2026 (multiple integrators, 72-hour edit window) comes from a secondary source only.
