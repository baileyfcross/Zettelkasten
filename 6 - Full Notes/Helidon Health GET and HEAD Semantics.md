2026-10-19 22:48

Status: #baby

Tags: [[Helidon Fault Tolerance and Health]]

# Helidon Health GET and HEAD Semantics

A GET request to a Helidon health endpoint returns JSON containing the detailed results of the checks executed for that path. This is suitable for a person or monitoring client that needs the names, statuses, and diagnostic data behind the aggregate result.

A HEAD request executes the health decision but returns only the HTTP status and no payload. The two methods expose the same operational judgment with different response detail.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
