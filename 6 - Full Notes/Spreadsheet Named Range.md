2026-09-28 23:03

Status: #baby

Tags: [[Game Design Spreadsheets]] [[Excel Formula Analysis and Automation]]

# Spreadsheet Named Range

A spreadsheet named range assigns a meaningful identifier to a cell or block of cells so formulas and validation rules can refer to it without opaque coordinates. A name such as `CargoWeight` or `MonsterNames` communicates purpose and can be used throughout the workbook.

Named ranges are workbook-global and dynamic: dependent formulas or drop-downs see changes to the values inside the range. Their identifiers must therefore be unique and follow spreadsheet naming restrictions, such as avoiding spaces. Naming improves readability, but the underlying values still need labels and a stable home such as a [[Spreadsheet Reference Sheet]].

In Excel, named ranges can connect interface controls to calculation logic. One range can hold the allowed company names for a combo box, while a parallel data range supplies the values retrieved by INDEX from the selected position. This makes a worksheet interaction easier to read than raw coordinates, provided that the named ranges remain aligned and their workbook scope is understood.

# References

[[introductiontogamesystemdesign.pdf]]

[[microsoftexcelfunctionsandformulaswithexcel2019andoffice365.pdf]]
