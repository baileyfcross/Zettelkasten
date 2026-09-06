2026-09-06 18:44

Status: #baby

Tags: [[Analytic Data Preparation]]

# Dataset Structure Check

A dataset structure check verifies the shape and schema of data immediately after import. It compares observed row and column counts, names, classes, storage modes, levels, and missingness with the expected metadata.

This check catches silent transformations such as renamed variables, unexpected factor conversion, or a source field read with the wrong type. Later statistical output cannot repair a mismatch introduced at import, so structural validation belongs at the beginning of the pipeline.

# References

[[analyzinghealthdatainrforsasusers.pdf]]
