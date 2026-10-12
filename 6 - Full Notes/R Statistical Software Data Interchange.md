2026-10-04 22:20

Status: #baby

Tags: [[R Data Interchange and External Formats]]

# R Statistical Software Data Interchange

R statistical software data interchange converts datasets produced by SAS, SPSS, Stata, or Systat into R objects and, where supported, exports R data back to those formats. Successful transfer requires more than readable rows: variable labels, value labels, missing-value codes, dates, and categorical encodings may not map identically between systems.

The imported object should therefore undergo the same structural and class review as any other [[R Data Import]]. Format-specific readers are preferable to assuming that a proprietary file behaves like ordinary text.

# References

[[rprimer.pdf]]
