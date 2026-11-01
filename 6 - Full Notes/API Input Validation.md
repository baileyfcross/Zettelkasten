2026-10-31 21:16

Status: #baby

Tags: [[REST API Security and Access Control]]

# API Input Validation

API input validation checks an untrusted request against the expected type, required fields, ranges, formats, and business rules before application behavior or persistence uses it. Rejected input should receive a clear client-error response.

The book demonstrates schema and serializer validation across frameworks and recommends validating path, query, header, and body values. Validation protects data integrity and narrows the attack surface, but it must be enforced on the server even when a client interface performs its own checks.

# References

[[masteringrestapis.epub]]
