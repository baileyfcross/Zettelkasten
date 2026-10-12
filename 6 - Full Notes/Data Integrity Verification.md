2026-09-14 02:44

Status: #baby

Tags: [[Cybersecurity Goals and Trust]]

# Data Integrity Verification

Data integrity verification checks that information remains the same across storage, transmission, or processing. A sender can calculate a [[Cryptographic Hash Function|cryptographic hash]], and a recipient can recompute it and compare the result with a trusted original digest.

Matching hashes support evidence that the data was not altered, but an unkeyed hash alone does not establish who supplied it. Authentication or a signature is required when origin matters as well as content.

# References

[[cybersecurity.epub]]
