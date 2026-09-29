2026-09-28 21:33

Status: #baby

Tags: [[Reproducible Scientific Software]]

# Clean Working Tree for Computational Runs

A clean working tree policy permits an official computational run only when all relevant code changes have been committed. The recorded revision then fully describes the code state, making the [[Research Software Version-to-Result Link]] unambiguous.

When exploratory work must run with uncommitted changes, an alternative is to capture the exact diff alongside the record. Refusing or documenting dirty runs prevents invisible local edits from producing results that cannot be reconstructed from the repository. The policy concerns traceability, not the scientific correctness of the code.

# References

[[implementingreproducableresearch.pdf]]
