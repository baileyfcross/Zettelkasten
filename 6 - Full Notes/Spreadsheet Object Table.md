2026-09-28 23:03

Status: #baby

Tags: [[Game Design Spreadsheets]]

# Spreadsheet Object Table

A spreadsheet object table places one game data object in each row and one attribute in each column. The first column commonly identifies the object, while the remaining column headers define the schema shared by objects of that type.

The inverse layout is computationally possible, but rows-for-objects is the established game-data convention and is commonly expected by import tools. It also accommodates the usual case in which a game has more objects than attributes. Categories should be encoded as attributes rather than represented by blank separator rows, because blank rows interrupt fills, filters, counts, and exports.

# References

[[introductiontogamesystemdesign.pdf]]
