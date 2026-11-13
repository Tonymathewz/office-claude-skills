# Bangladesh (BD) — invoice & bookkeeping profile

> Last checked: 2026-11-13. Rules change often. Not tax advice: confirm anything important with a local accountant or NBR.

## At a glance
| Item | Value |
|---|---|
| Tax name | Value Added Tax (VAT) and Supplementary Duty (SD) under the VAT & SD Act 2012 / VAT & SD Rules 2016. Turnover Tax for small "enlisted" businesses |
| Tax authority | National Board of Revenue (NBR), https://nbr.gov.bd. Online system: e-VAT (vat.gov.bd) |
| Rates | **15%** standard. Reduced (truncated) rates 10%, 7.5%, 5% for listed supplies (Third Schedule). Trading-stage and sector-specific rates (e.g. some trading 7.5%, medicines 3%, petroleum 2%). Fixed amounts per unit for some goods (e.g. gold per bhori from FY27). 0% for exports. Exempt: First Schedule. Imported services: 15% reverse charge |
| Registration threshold | VAT registration mandatory above **BDT 50 lakh** (5 million) annual turnover (since 9 Jan 2025). **Enlistment** (Turnover Tax **4%**, no input credit) for BDT 30–50 lakh. Below BDT 30 lakh: outside VAT. Since the Finance Act 2026, a BIN or enlistment number is needed for bank accounts, loans, trade licence renewal etc. |
| Currency | BDT |
| Tax ID name & format | **BIN** (Business Identification Number). The e-VAT system issues a 9-digit BIN. Branch/unit-level and some published references use 13 digits. Treat `^\d{9}(-?\d{4})?$` as acceptable and verify online |
| Online tax-ID check | BIN search on the NBR / e-VAT website |
| Filing frequency & deadline | **Mushak 9.1** return (Mushak 9.1.1 for traders not claiming input credit). Frequency changed in 2026: the Finance Act 2026 moved returns to **quarterly** (15 days after the quarter). Reports say an ordinance/amendment restored **monthly** returns (by the 15th of the next month) from the Oct 2026 period. **Confirm with accountant.** Pay before filing |
| Record retention | 5 years (s.107), longer if proceedings are pending. Electronic/ERP records are accepted (s.107(2A), FA 2026) |

## Full tax invoice: required fields
**Mushak 6.3** (tax invoice), issued on or before the time VAT becomes payable, in at least 2 copies:
1. Supplier name, address, **BIN**.
2. Invoice serial number (sequential within the fiscal year).
3. Date **and time** of issue (often missed).
4. Buyer name, address and **BIN**: required where the supply exceeds **Tk 25,000** or the buyer is registered (needed for the buyer's input credit).
5. Description, quantity, unit price of goods/services.
6. Value excluding VAT; SD (if any); VAT rate and amount; total including VAT.
7. Vehicle details / delivery destination for goods dispatched (as on the form).
8. Authorised signature.
- Supplies above **Tk 2 lakh** are also reported on **Mushak 6.10**.

## Simplified invoice / receipt
- Retail/consumer sales: for businesses in the mandated categories and areas, the receipt must come from an **EFD/SDC or NBR-approved POS**: a QR-coded, digitally signed "VAT smart challan" (Mushak 6.3 equivalent). Mandated since 2019 for 27 listed business types (restaurants, supermarkets, etc.) in named districts/city corporations.
- Enlisted (turnover-tax) businesses can't charge VAT and their buyers can't claim input credit.
- Buyers claim input credit only on a proper Mushak 6.3 (or the import bill of entry) showing their BIN.

## Credit and debit notes
- **Mushak 6.7** = credit note, **Mushak 6.8** = debit note. Used for returns, price changes or cancellations. They must reference the original Mushak 6.3 (number and date).
- If the VAT effect exceeds **Tk 5,000**, the note must show the recipient's details (name, address, BIN).
- Adjustments go in the return as increasing/decreasing adjustments. Time limit: see Confidence notes.
- Other key forms: **6.1** purchase register, **6.2** sales register, **6.2.1** combined purchase-sales register, **6.5** transfer between branches, **6.6** VAT deducted at source (VDS) certificate, **4.3** input-output coefficient (manufacturers).

## E-invoicing / clearance status (as of last-checked date)
- No nationwide B2B clearance e-invoicing. Instead: the **e-VAT** online registration and return system, plus mandatory **EFD/SDC/POS** fiscal devices for listed retail/service categories, producing QR-coded, signed receipts reported to NBR.
- NBR may mandate electronic return filing for specified manufacturers/service providers (reported Sept 2026).
- **The skill must NEVER fabricate an EFD/SDC receipt number, QR code, BIN or Mushak 6.6 VDS certificate.** It can draft a Mushak 6.3 layout for review, marked as a draft.

## Numbering & language
- Sequential serial numbers per fiscal year (July–June). Separate series per branch/unit is common.
- Mushak forms are bilingual (Bangla/English). English invoices are widely used. Keep the official form layout and field order.

## Reverse charge, imports & cross-border
- **Imported services:** 15% VAT under reverse charge. The recipient pays via bank challan, and the challan serves as the tax invoice/ITC document (FA 2026).
- **Imports of goods:** VAT, AT (advance tax) and SD are collected by Customs on the bill of entry.
- **VDS (withholding):** government bodies, banks, NGOs, listed companies etc. deduct VAT at source from suppliers and issue **Mushak 6.6**. The supplier uses 6.6 to reduce its own liability. Track every 6.6 received.
- Exports: zero-rated. Keep export documents (LC, bill of export).

## Checks the skill must run for this country
- Supplier BIN present and matches `^\d{9}(-?\d{4})?$`. Buyer BIN present when value > Tk 25,000 or the buyer is registered.
- The document is titled/structured as Mushak 6.3 (or an EFD/POS receipt for retail). Date **and time** are present.
- VAT rate is 15% unless a reduced/fixed rate is cited. Flag 5/7.5/10% without a schedule/category explanation.
- Arithmetic: value × rate = VAT (±1 BDT); (SD applied before VAT where applicable); total = value + SD + VAT.
- Purchase > Tk 2 lakh → also on Mushak 6.10. Flag input claims on purchases > Tk 1 lakh not paid through a bank channel (see Confidence notes).
- Credit/debit note is on Mushak 6.7/6.8, references the original 6.3 number and date, and shows buyer details if VAT > Tk 5,000.
- VDS: when the user's company is a withholding entity, VAT withheld and a Mushak 6.6 issued. When the user is the supplier, a 6.6 is received for each VDS deduction.
- Supplier is VAT-registered (not just enlisted) before input credit is claimed.

## Common mistakes
- Claiming input VAT on invoices without the buyer's BIN, or on enlisted/turnover-tax suppliers' bills.
- Missing Mushak 6.6 certificates for VDS → double payment of VAT.
- Not issuing 6.7/6.8 for returns/discounts, and just editing the original invoice.
- Using the wrong return frequency in 2026 (it changed twice).

## Sources
- https://lookuptax.com/docs/country/bangladesh-vat-guidelines-indirect-tax
- https://www.pwc.com/bd/en/assets/pdfs/budget/finance-act-2026-key-amendments.pdf
- https://www.dfdl.com/insights/legal-and-tax-updates/bangladesh-updates-on-amendments-to-the-vat-law/
- https://lookuptax.com/tax-changes/bangladesh/quarterly-vat-returns-2026
- https://www.dhakatribune.com/business/420880/nbr-to-return-to-monthly-vat-return-process (seen in search results only; not read)

## Confidence notes
- **Return frequency is the biggest uncertainty.** The Finance Act 2026 made returns quarterly from Jul 2026. A secondary source says Ordinance No. 38 of 2026 restored monthly returns from the Oct 2026 period. News headlines (Sept 2026) agree but weren't read in full.
- **BIN length:** sources say 13 digits; the e-VAT system issues 9-digit BINs (13 with branch suffix). Not verified on nbr.gov.bd (not fetched in this session).
- The input-credit time limit (believed: same period or the next 4 tax periods), the bank-channel condition for purchases over Tk 1 lakh, and any credit-note time limit were **not verified**.
- Trading-stage rate (5% vs 7.5%) is from a secondary source. Check the current Third Schedule.
- No official NBR page was read in this session. All facts come from professional-firm and secondary summaries.
