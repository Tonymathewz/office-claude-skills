# Singapore (SG) — invoice & bookkeeping profile

> Last checked: 2026-11-13. Rules change often. Not tax advice: confirm anything important with a local accountant or the tax authority.

## At a glance
| Item | Value |
|---|---|
| Tax name | Goods and Services Tax (GST) |
| Tax authority | Inland Revenue Authority of Singapore (IRAS) — https://www.iras.gov.sg |
| Rates | Standard 9% / zero-rated 0% (exports, international services) / exempt (e.g. certain financial services, residential property) / out-of-scope |
| Registration threshold | Compulsory when taxable turnover exceeds S$1 million (12-month retrospective or prospective basis); voluntary registration possible |
| Currency | SGD. Foreign-currency invoices allowed, but GST amount must be converted to SGD using an IRAS-approved exchange rate and shown in SGD |
| Tax ID name & format | GST Registration Number — usually the entity's UEN (e.g. `201912345K`), or an `M2-1234567-8` / `M9...` style number for entities without a UEN. Loose regex: `^(\d{8,9}[A-Z]|[STRF]\d{2}[A-Z]{2}\d{4}[A-Z]|M[0-9]-?\d{7}-?[0-9A-Z])$` |
| Online tax-ID check | IRAS "Check GST Registered Business" search on iras.gov.sg (search by name/UEN/GST no.) |
| Filing frequency & deadline | GST F5 return usually quarterly (monthly on request); file and pay within 1 month after the end of the accounting period |
| Record retention | At least 5 years |

## Full tax invoice: required fields
Issue within 30 days of the time of supply when selling standard-rated supplies to a GST-registered customer.
1. The words **"Tax Invoice"** in a prominent place (*often missed* — "Invoice" alone is not enough)
2. Supplier's name, address and **GST registration number**
3. Invoice identifying number
4. Date of issue
5. Customer's name and address
6. Description of goods/services
7. **GST rate** applied
8. Amount payable **excluding GST**, the **GST amount**, and amount **including GST** (*often missed* — all three must be shown)
9. For zero-rated items: a statement that GST is charged at 0%
10. For foreign-currency invoices: GST amount (and ideally totals) in SGD with the exchange rate used (*often missed*)

## Simplified invoice / receipt
- **Simplified tax invoice**: allowed only where total payable **including GST does not exceed S$1,000**. Fields: supplier name, address, GST reg no.; invoice number; date; description; total including GST; statement that "price payable includes GST". A GST-registered buyer can generally claim input tax on it.
- **Receipt**: only for customers who are **not** GST-registered. Must be serially printed, show date, supplier name, GST reg no., total including GST, and "Price payable includes GST". Keep a duplicate.

## Credit and debit notes
Credit note fields: identifying number and date; supplier name, address, GST reg no.; customer name and address; **number and date of the original tax invoice**; description, quantity and amount credited; GST rate, GST credited, total credited incl. GST. If the original invoice number cannot be shown, keep other evidence that GST was accounted for. Foreign-currency credit notes normally use the exchange rate of the original invoice (customer may use prevailing rate; be consistent). The title "Credit Note" is mandatory only for credit notes linked to a rate change.

## E-invoicing / clearance status (as of last-checked date)
- **System**: InvoiceNow (IMDA's nationwide Peppol network). The **GST InvoiceNow Requirement** = GST-registered businesses send invoice **data** to IRAS via an InvoiceNow-ready solution / Peppol Access Point. It is a **reporting** model, not pre-clearance: the invoice is not "approved" by IRAS before issue.
- **Phases** (IRAS, Committee of Supply 2026):
  - 1 May 2025: soft launch, voluntary
  - 1 Nov 2025: newly incorporated companies registering for GST voluntarily
  - 1 Apr 2026: **all new voluntary GST registrants**
  - 1 Apr 2028: all new compulsory registrants + existing registrants with annual supplies ≤ S$200,000
  - 1 Apr 2029: existing registrants ≤ S$1 million
  - 1 Apr 2030: existing registrants ≤ S$4 million
  - 1 Apr 2031: existing registrants > S$4 million
- Needs: Peppol ID registered against the UEN, an IMDA-accredited solution connected to IRAS.
- **The skill must NOT** invent Peppol IDs, transmission confirmations or IRAS acknowledgement references, or claim an invoice "was sent to IRAS". It can only check whether the user's in-scope status means they must transmit, and remind them to issue through their InvoiceNow solution.

## Numbering & language
- Unique, sequential identifying numbers; multiple series/prefixes are acceptable if each is unique and traceable.
- No mandatory language stated by IRAS; English is standard in practice.

## Reverse charge, imports & cross-border
- Imported services and low-value goods bought from overseas suppliers: **reverse charge** applies to GST-registered businesses that are not entitled to full input tax credit (e.g. partly exempt businesses, charities). The buyer self-accounts output tax and claims input tax per normal rules.
- Overseas vendors selling B2C digital services / low-value goods to Singapore may be registered under the Overseas Vendor Registration regime — their invoices to Singapore businesses may still show 9% GST.
- Exports: zero-rated (0%) with export evidence kept.

## Checks the skill must run for this country
- GST is computed at 9% for supplies with time of supply on/after 1 Jan 2024; flag 7% or 8% unless the user confirms an older time of supply.
- Purchase invoice used to claim input tax shows "Tax Invoice", supplier GST reg no., and GST amount separately — otherwise flag "cannot claim input tax on this document as-is".
- Supplier GST reg no. matches the loose format regex; prompt user to check it in the IRAS GST register (do not claim it is verified).
- If total incl. GST > S$1,000 and the document is a simplified tax invoice / receipt, flag: full tax invoice needed.
- Line maths: Σ(excl.-GST lines) + GST = total incl. GST (tolerance ±S$0.01 per line rounding).
- Foreign-currency invoice: GST amount shown in SGD; exchange rate recorded.
- Sales invoices issued by the user: include all 10 fields above; issued ≤30 days after time of supply.
- Credit note references original invoice number and date.
- InvoiceNow scope: ask registration date/type and annual supplies; if in scope (e.g. new voluntary registrant on/after 1 Apr 2026), remind that invoice data must be sent via their InvoiceNow solution.
- Supplier charging GST but not in IRAS register: flag as possible improper GST charge.

## Common mistakes
- Claiming input tax on a supplier's receipt or quotation instead of a tax invoice.
- Using "Invoice" rather than "Tax Invoice".
- Foreign-currency invoices with no SGD GST amount.
- Paying GST to a supplier who isn't GST-registered.
- Forgetting reverse charge on overseas software/services when partly exempt.

## Sources
- https://www.iras.gov.sg/news-events/newsroom/committee-of-supply-2026--extension-of-gst-invoicenow-requirement-to-all-gst-registered-businesses-by-april-2031
- https://www.iras.gov.sg/taxes/goods-services-tax-(gst)/basics-of-gst/invoicing-price-display-and-record-keeping/invoicing-customers
- https://www.gobusiness.gov.sg/news-and-updates/news/gst-invoicenow-requirement

## Confidence notes
- Verified from IRAS pages: invoice/receipt/credit-note fields, S$1,000 simplified threshold, 30-day rule, SGD conversion, InvoiceNow phase dates.
- Not re-verified this session (well established, but check iras.gov.sg): 9% rate start date, S$1m registration threshold, quarterly filing deadline, 5-year retention, reverse charge scope, GST number format/regex.
- Unverified: whether purchase-invoice data must also be transmitted, and how InvoiceNow handles sales to customers not on Peppol / B2C — confirm in the IRAS "GST InvoiceNow Requirement" guide.
- Language requirement: IRAS page states none; English assumed.
