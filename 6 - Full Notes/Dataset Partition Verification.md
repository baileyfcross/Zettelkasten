2026-09-06 18:44

Status: #baby

Tags: [[Analytic Data Preparation]]

# Dataset Partition Verification

Dataset partition verification checks that records divided into retained and excluded groups still account for the original dataset. A basic test compares the original row count with the sum of the output partition counts.

This arithmetic invariant detects gaps and overlaps created by incorrect Boolean conditions or missing-value behavior. Passing it does not prove that the substantive criteria are correct, but failing it proves that the split was not implemented as intended.

# References

[[analyzinghealthdatainrforsasusers.pdf]]
