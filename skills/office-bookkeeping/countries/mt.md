# Malta (MT) - invoice & bookkeeping profile

> Last checked: 2026-11-13. Also read `eu.md`. Not tax advice: confirm with a warranted accountant or the MTCA.

## At a glance
| Item | Value |
|---|---|
| Tax name | VAT |
| Tax authority | Malta Tax and Customs Administration (MTCA, formerly CfR); VAT Act Chapter 406 |
| Rates | 18% standard; 12%, 7%, 5% reduced; 0% exempt with credit (e.g. exports, intra-EU supplies); exempt without credit |
| Registration threshold | Article 11 small undertaking: domestic turnover up to EUR 35,000 (from 1 Jan 2025) |
| Currency | Invoices may be in any currency, but the VAT must also be shown in euro |
| Tax ID | VAT number: `MT` + 8 digits (regex `^MT\d{8}$`) |
| Online tax-ID check | VIES: https://ec.europa.eu/taxation_customs/vies/ |
| Filing | Article 10: usually quarterly, due 6 weeks after the period ends. Article 11: annual declaration by 15 March |
| Record retention | At least 6 years from the end of the year the records relate to (VAT Act Art. 48(4)); can be longer |

## Registration types (decide what invoices may show)
- **Article 10 (full)**: charges VAT, issues full tax invoices, recovers input VAT.
- **Article 11 (small undertaking, exempt)**: must NOT charge or show VAT; cannot recover input VAT. Fiscal receipts mark exempt lines "E"/"Exempt" (see confidence notes).
- **Article 12 (EU transactions only)**: for exempt or Article 11 persons with intra-EU acquisitions over EUR 10,000 a year or reverse-charge services. Self-accounts VAT on those purchases, can't recover it. Their own sales invoices still show no VAT.

## Full tax invoice: required fields (Twelfth Schedule)
EU Art. 226 fields (see `eu.md`), in particular:
1. Issue date and sequential number
2. Name, address and VAT number of supplier **and customer**
3. Quantity and nature of the supply, and the supply date
4. Taxable value per rate, rate, and VAT amount (VAT in euro)
5. Where relevant: "Cash Accounting", "Self-billing", "Reverse Charge", "Margin Scheme", or the exemption provision

## Simplified invoice / fiscal receipt
- Fiscal receipts are used where no tax invoice is issued (mainly B2C).
- **A fiscal receipt does not support an input VAT claim.** For business purchases, ask the supplier for a proper tax invoice.

## Credit and debit notes
Must refer to the original invoice (EU rule).

## E-invoicing status
No mandatory B2B or B2C e-invoicing yet. Public bodies accept EN 16931 e-invoices (Peppol BIS Billing 3.0). The MTCA is preparing mandatory e-invoicing and real-time reporting, but no official dates have been announced (unverified as of Nov 2026).

## Checks the skill must run
- For any purchase where VAT is to be claimed: a **tax invoice** (not a fiscal receipt) showing the supplier's MT VAT number AND the buyer's name and VAT number.
- VAT rate is one of 18/12/7/5/0.
- Business on Article 11: sales invoices show no VAT; purchase VAT is a cost (not claimable).
- Foreign-currency invoice: the VAT amount is also shown in EUR.
- Supplier abroad + no VAT charged: flag reverse charge (Article 10 or 12 business self-accounts). `ASK ACCOUNTANT` if unsure.

## Common mistakes
- Claiming VAT on fiscal receipts or manual receipts. A February 2026 tribunal case denied a transport business's input VAT for this reason.
- Article 11 businesses showing VAT on invoices.
- Missing customer VAT number on B2B invoices.

## Sources
- https://pwc.com/mt/en/publications/vat/updates-to-the-vat-effective-1-january-2025.html
- https://taxsummaries.pwc.com/malta/corporate/other-taxes
- https://www.csbgroup.com/vat-services-malta/vat-returns-and-rates/
- https://www.vatupdate.com/2026/02/17/malta-tribunal-upholds-strict-vat-invoice-rules-in-transport-services-dispute/
- https://www.deloitte.com/mt/en/services/tax/perspectives/e-invoicing-in-malta.html

## Confidence notes
- The national deadline for issuing domestic invoices was not verified.
- The 2026 rule that Article 11 fiscal receipts show "EXP" before the VAT number comes from a secondary summary only. Verify it with the MTCA.
- Field list taken from secondary sources (MIT lecture notes, PwC). Check against the current Twelfth Schedule.
