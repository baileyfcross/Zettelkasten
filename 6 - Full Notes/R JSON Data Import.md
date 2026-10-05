2026-10-04 22:20

Status: #baby

Tags: [[R Data Interchange and External Formats]]

# R JSON Data Import

R JSON data import parses JavaScript Object Notation into R lists, vectors, or data frames according to the nesting and types in the document. Flat arrays of similarly shaped records can simplify into a table, while nested or heterogeneous structures need explicit navigation before they become rectangular data.

Automatic simplification should be checked rather than assumed. Names, null values, numeric coercion, and nested arrays can change the resulting R structure, so inspection must precede transformation or modeling.

# References

[[rprimer.pdf]]
