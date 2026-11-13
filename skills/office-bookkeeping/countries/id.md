# Indonesia (ID) — invoice & bookkeeping profile

> Last checked: 2026-11-13. Rules change often. Not tax advice: confirm anything important with a local accountant or the tax authority.

## At a glance
| Item | Value |
|---|---|
| Tax name | Pajak Pertambahan Nilai (PPN, VAT); plus PPnBM (luxury-goods sales tax) on some goods |
| Tax authority | Direktorat Jenderal Pajak (DJP) — https://www.pajak.go.id |
| Rates | Statutory **12%**. In practice (PMK 131/2024, from 1 Jan 2025): **non-luxury goods/services → 12% × DPP "nilai lain" of 11/12 of price = effective 11%**; luxury goods subject to PPnBM → 12% × full price (from 1 Feb 2025). 0% for exports; exempt / "not collected" (DTP) facilities exist |
| Registration threshold | Must become PKP (Pengusaha Kena Pajak) when turnover exceeds Rp4.8 billion/year; voluntary PKP possible |
| Currency | IDR. Foreign-currency transactions must be converted to IDR at the Ministry of Finance (KMK) rate for tax purposes |
| Tax ID name & format | **NPWP 16 digits** (companies, non-residents, government; old 15-digit NPWP + leading `0`); resident individuals use **NIK** (16-digit national ID) as NPWP; **NITKU 22 digits** (= NPWP + 6-digit place-of-business number) identifies the branch/location. Regex: NPWP/NIK `^\d{16}$`, NITKU `^\d{22}$` |
| Online tax-ID check | Coretax DJP (coretaxdjp.pajak.go.id) / ereg NPWP check — via the user's own login |
| Filing frequency & deadline | Monthly VAT return (SPT Masa PPN) via Coretax; faktur upload by the 15th of the following month; return due end of the following month |
| Record retention | 10 years |

## Full tax invoice: required fields
In Indonesia the VAT invoice is the **Faktur Pajak**, which must be created **electronically in Coretax (e-Faktur module)**. A commercial invoice alone does not support input-tax credit. Required content:
1. Name, address, NPWP (and NITKU) of the PKP seller
2. Buyer name, address and NPWP/NIK (and NITKU) — *often missed*: buyer must give NIK/NPWP; passport for foreign individuals
3. **17-digit code + serial number**: 2-digit transaction code + 2-digit status code + 13-digit serial (first 2 digits = year). The serial is **assigned automatically by DJP** when the faktur is uploaded and approved
4. Transaction code (see below) — *often wrong*: non-luxury sales computed on 11/12 DPP must use **code 04**
5. Item name/type, unit, quantity, unit price, discount
6. Selling price / reimbursement, **DPP** (tax base), PPN amount, PPnBM if any
7. Date of faktur
8. Electronic signature of the PKP (applied in Coretax)

Transaction codes (PER-11/PJ/2025): 01 normal; 02 to government VAT collector; 03 to other VAT collectors; **04 DPP nilai lain (incl. 11/12)**; 05 deemed/fixed-rate VAT; 06 tourist refund; 07 not-collected / government-borne facility; 08 exempt; 09 fixed-asset transfer; 10 other (e.g. non-standard rate).

Worked example (code 04): price Rp12,000,000 → DPP 11/12 = Rp11,000,000 → PPN 12% = Rp1,320,000.

## Simplified invoice / receipt
Retail PKPs selling to end consumers may issue simplified invoices (cash register receipts / "faktur pajak digunggung") without buyer identity; these are reported in aggregate. **Buyers cannot claim input VAT** on them — a business buyer needs a full Faktur Pajak with its NPWP.

## Credit and debit notes
Returns/cancellations: buyer issues a **Nota Retur**, or seller cancels/replaces the faktur in Coretax (**faktur pengganti** = status code for replacement; cancellation via the system). Must reference the original faktur number. Done in Coretax; do not edit PDFs.

## E-invoicing / clearance status (as of last-checked date)
- **System**: Coretax DJP (live since 1 Jan 2025) with integrated e-Faktur module. Faktur Pajak exists only once uploaded, approved and signed in Coretax — this is effectively **clearance**: DJP assigns the serial number (NSFP) and the PDF carries DJP's QR code.
- Applies to **all PKPs** for VAT invoices (no size phase-in).
- **The skill must NOT** fabricate faktur serial numbers, QR codes, approval status or Coretax references. The user must create/approve the faktur in Coretax (or via a DJP-certified PJAP provider). The skill can prepare a data sheet and check codes, DPP and maths.

## Numbering & language
- Faktur serial numbers are system-assigned (not user-chosen). Commercial invoice numbers are the seller's own sequence.
- Faktur content is in Indonesian (Coretax output); commercial invoices may be bilingual.

## Reverse charge, imports & cross-border
- Imported services / intangibles from abroad: the Indonesian buyer **self-assesses PPN** (pay with SSP/billing code, then credit as input tax if eligible) — PPN on "pemanfaatan JKP/BKP tidak berwujud dari luar daerah pabean".
- Foreign digital (PMSE) providers appointed by DJP collect PPN directly.
- Import VAT is collected by Customs (PIB is the tax document).

## Checks the skill must run for this country
- Seller NPWP is 16 digits (or NIK 16 digits); NITKU, if shown, is 22 digits and starts with the NPWP.
- Input-tax claim only if a Faktur Pajak exists (17-digit code+serial `^\d{2}\d{2}\d{13}$` or with separators) — commercial invoice alone → flag.
- For transaction code 04 with PMK 131: DPP = round(price × 11/12) and PPN = DPP × 12% (≈ 11% of price). Flag 12% on full price for non-luxury goods, and flag 11% "rate" written on new fakturs.
- For luxury (PPnBM) goods: PPN = 12% × full price; PPnBM shown separately.
- Transaction code matches buyer type (02 for government collector, 03 for other collectors, 07/08 for facility/exempt).
- Faktur date is in the same month as the delivery/payment; upload no later than the 15th of the next month.
- Buyer identity on faktur = the user's company NPWP/NITKU exactly (wrong NPWP → not creditable).
- Foreign-currency invoices converted at the KMK weekly rate.
- Never present a faktur number or QR as valid unless copied from the user's Coretax document.

## Common mistakes
- Charging a flat 12% on the full price for ordinary goods (overcharges buyers).
- Using code 01 instead of 04 for the 11/12 mechanism.
- Accepting a faktur with the wrong buyer NPWP or old 15-digit format.
- Forgetting self-assessed PPN on foreign services/software.
- Late faktur upload (input tax can be denied, penalties apply).

## Sources
- https://news.ddtc.co.id/berita/nasional/1807939/pmk-terbaru-soal-ppn-12-akhirnya-terbit-begini-perinciannya
- https://news.ddtc.co.id/berita/nasional/1808027/hitung-ppn-pakai-dpp-1112-harga-jual-perhatikan-lagi-kode-fakturnya
- https://news.ddtc.co.id/berita/nasional/1811127/per-11pj2025-pertegas-ketentuan-kode-dan-nomor-seri-faktur-pajak
- https://news.ddtc.co.id/berita/nasional/1812992/tak-berubah-tarif-ppn-12-tetap-berlaku-untuk-barang-mewah-di-2026
- https://news.ddtc.co.id/literasi/kamus/1803684/apa-beda-nik-sebagai-npwp-npwp-16-digit-dan-nitku
- https://voffice.co.id/blog/en/how-to-create-a-tax-invoice-in-coretax/

## Confidence notes
- Sources are reputable Indonesian tax media (DDTC), not pajak.go.id itself; official PMK/PER texts were not opened.
- "No change in 2026" for the 11/12 mechanism is from an Aug 2025 statement; I found no 2026 regulation changing it, but a rate cut was being discussed in 2026 — **re-check before relying on it**.
- PKP threshold Rp4.8bn, 10-year retention, return due date, KMK rate rule, simplified/digunggung details and Nota Retur mechanics are from background knowledge, not verified this session.
- Effective date of PER-11/PJ/2025 transaction codes not confirmed.
