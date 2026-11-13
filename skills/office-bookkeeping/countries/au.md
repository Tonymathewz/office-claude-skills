# Australia (AU) — invoice & bookkeeping profile

> Last checked: 2026-11-13. Rules change often. Not tax advice: confirm anything important with a local accountant or the tax authority.

## At a glance
| Item | Value |
|---|---|
| Tax name | Goods and Services Tax (GST) |
| Tax authority | Australian Taxation Office (ATO) — https://www.ato.gov.au |
| Rates | 10% standard (GST = 1/11 of a GST-inclusive price); GST-free (0%) items; input-taxed items (no GST, no credit) |
| Registration threshold | GST turnover A$75,000 (non-profits A$150,000); overseas businesses selling to Australian consumers A$75,000; taxi/limousine/ride-sourcing must register regardless |
| Currency | AUD normal; for foreign-currency invoices see Confidence notes |
| Tax ID name & format | Australian Business Number (ABN): 11 digits, often written `XX XXX XXX XXX`. Regex `^\d{2} ?\d{3} ?\d{3} ?\d{3}$`. For companies, ABN = 2 check digits + 9-digit ACN |
| Online tax-ID check | ABN Lookup: https://abr.business.gov.au (also shows whether registered for GST and from when) |
| Filing frequency & deadline | Business Activity Statement (BAS) monthly, quarterly or annually depending on turnover/election (see Confidence notes) |
| Record retention | 5 years (written, English or easily translatable, paper or electronic) |

## Full tax invoice: required fields
Tax invoice (sales under A$1,000) must let you identify:
1. That it is intended to be a **tax invoice**
2. Seller's identity
3. **Seller's ABN** (often missing on small-supplier invoices)
4. Date of issue
5. Brief description, quantity (if applicable) and price
6. GST amount, **or** "Total price includes GST" where GST is exactly 1/11 of the total
7. Extent to which each item is taxable (mixed invoices: mark taxable vs GST-free/input-taxed)
**Sales of A$1,000 or more (GST-inclusive):** also the **buyer's identity or ABN** (most-missed field).
- Supplier must give a tax invoice within 28 days of request, unless the sale is A$82.50 (incl. GST) or less.
- Buyer generally needs a valid tax invoice to claim a GST credit when the purchase is over A$82.50.

## Simplified invoice / receipt
- For purchases of A$82.50 (incl. GST) or less, a receipt/cash register docket is enough to claim the credit (keep it).
- Invoices from suppliers **not registered for GST** are not tax invoices and must not include GST → no credit.

## Credit and debit notes
- Called **adjustment notes**. A valid adjustment note is generally needed before claiming a decreasing adjustment, unless the GST adjustment is A$75 or less.
- If you don't hold the note when lodging the BAS, claim it in the first BAS after receiving it.
- No decreasing adjustment for a transaction that never included GST, even if a document is called an adjustment note.
- Recipient-created tax invoices (RCTIs): only with a written agreement, both parties GST-registered, Commissioner approval for that supply type; marked "recipient created tax invoice", showing both ABNs; issued within 28 days.

## E-invoicing / clearance status (as of last-checked date)
- **Peppol** is the national e-invoicing network (A-NZ PINT spec); access via an ATO-accredited Peppol service provider.
- **Voluntary for B2B.** Commonwealth agencies: target 30% of supplier invoices via Peppol by mid-2026; agencies to receive and send Peppol e-invoices by Dec 2026.
- A Peppol e-invoice following the A-NZ spec can be a valid tax invoice even without the words "tax invoice".
- No clearance/QR/UUID requirement. The skill must not invent ABNs or Peppol participant IDs.

## Numbering & language
- No mandatory sequential numbering, but unique numbers are standard practice.
- Records in English (or easily convertible).

## Reverse charge, imports & cross-border
- Imported services/digital products: a GST-registered business buying from overseas generally self-assesses GST only if it would not get a full input credit (e.g. input-taxed or private use) — see Confidence notes.
- Import GST on goods paid to Home Affairs/Customs (or deferred via the ATO); the import declaration supports the credit.

## Checks the skill must run for this country
- ABN is 11 digits and passes checksum: subtract 1 from first digit, multiply digits by weights 10,1,3,5,7,9,11,13,15,17,19, sum mod 89 = 0. Test vector: 53 004 085 616 → sum 445 → valid.
- Prompt user to confirm on ABN Lookup that the supplier was **registered for GST on the invoice date**; if not, GST shown is not claimable.
- Invoice says "tax invoice" (or is a Peppol A-NZ e-invoice).
- GST = 10% of GST-exclusive amount, or 1/11 of inclusive total (±1 cent per line).
- Total incl. GST ≥ A$1,000 → buyer name or ABN present.
- Purchase > A$82.50 incl. GST with GST claimed → tax invoice on file.
- Mixed supplies: each line marked taxable / GST-free / input-taxed.
- Our sales invoices: if we are not GST-registered, no GST line and not titled "tax invoice".
- Decreasing adjustment with GST > A$75 → adjustment note on file.

## Common mistakes
- Claiming GST from a supplier whose ABN is active but not GST-registered.
- Missing buyer details on A$1,000+ invoices.
- Claiming GST credits on overseas invoices with no GST.
- Treating a statement or quote as a tax invoice.

## Sources
- https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/tax-invoices (fields, A$1,000 rule, A$82.50, 28 days, RCTI)
- https://www.ato.gov.au/businesses-and-organisations/gst-excise-and-indirect-taxes/gst/completing-your-bas-for-gst/making-adjustments-on-your-activity-statements/adjustment-notes (A$75 threshold)
- https://www.ato.gov.au/General/Other-languages/In-detail/Information-in-other-languages/Record-keeping-for-small-businesses/ (5-year retention, English, GST records)
- https://business.gov.au/registrations/register-for-goods-and-services-tax-gst (thresholds, taxi rule, 10%)
- https://lookuptax.com/docs/tax-identification-number/australia-tax-id-guide (ABN mod-89 algorithm, test vector, ABN Lookup)
- https://www.avalara.com/us/en/blog/australia-e-invoicing-2026-deadlines-government-adoption.html (Peppol government targets 2026)

## Confidence notes
- ABR's own ABN-format help page could not be opened (blocked); algorithm from secondary source.
- Purchase-side A$82.50 rule (no tax invoice needed to claim) is from general knowledge; the ATO page I read covers the supplier's 28-day duty.
- BAS frequency rules (monthly if turnover ≥ A$20m) and due dates not verified this session.
- Foreign-currency tax invoice rules (GST shown in AUD) and reverse-charge scope not verified.
- Government Peppol targets are from a vendor blog (Avalara), not a government page.
