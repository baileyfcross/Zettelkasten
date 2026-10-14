2026-10-07 17:18

Status: #baby

Tags: [[R Programming Environment]]

# R File Input and Output

R file input and output translates external text into typed R objects and writes analysis results back to persistent files. read.table handles rectangular records with configurable separators, headers, row names, comments, and missing-value markers, while scan provides lower-level sequential reading.

write.table preserves tabular structure and can control names, quoting, separators, and append behavior. A reliable workflow specifies these assumptions explicitly so a later import reconstructs the intended rows, columns, types, and missing values.

# References

[[statisticalcomputingincplusplusandr.pdf]]
