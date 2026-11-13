# Generic profile (country not covered yet)

> Use this only when there's no file for the business's country. Tell the user: "I don't have detailed rules for <country>, so I'll run basic checks only. Please confirm the invoice requirements with your accountant."

## Basic checks for any invoice anywhere
- Supplier's legal name and address, and tax/registration number if the country has one
- Buyer's name (and tax number for business purchases, where the country uses them)
- Unique invoice number and issue date
- Description, quantity and price of what was supplied
- Net amount, tax rate and tax amount per rate (if there is a sales tax, VAT or GST), and the total
- Currency
- Arithmetic adds up

## Questions to ask the user (and save in `setup.md` under "Rules learned")
1. Does your country have VAT/GST/sales tax? What are the rates?
2. What must a business invoice show for you to claim the tax back?
3. Is e-invoicing or government clearance (QR code, approval number) required? If yes, invoices must be issued through that system.
4. How many years must you keep records?
5. Is withholding tax deducted from some payments?

## Contribute
If you know your country's rules, copy `_TEMPLATE.md`, fill it in with official sources, and open a pull request.
