2026-10-19 22:48

Status: #baby

Tags: [[Helidon Database Client]]

# Helidon Named Database Statement

A Helidon named database statement assigns a stable configuration key to a database-specific query or operation. Application code refers to names such as `select-all`, `select-one`, `insert2`, or `delete-all` instead of embedding the complete SQL or MongoDB operation in the method.

Moving the statement into configuration allows different environments or database implementations to provide distinct native expressions without recompiling the application. Stable names also improve observability because metrics and traces can identify an operation semantically.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
