2026-10-04 22:20

Status: #baby

Tags: [[R Data Interchange and External Formats]]

# R Clipboard Data Import

R clipboard data import treats copied tabular text as an input connection so a small table can be read without first saving an intermediate file. The copied region still needs a predictable delimiter, header, and rectangular shape, and platform-specific connection names make the technique less portable than an explicit file-based [[R Data Import]].

Clipboard import is useful for brief interactive transfers, but a durable analysis should preserve the original data or export the copied content so that the step can be reproduced.

# References

[[rprimer.pdf]]
