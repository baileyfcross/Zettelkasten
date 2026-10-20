2026-10-19 22:48

Status: #baby

Tags: [[Helidon Fault Tolerance and Health]]

# Helidon Health HTTP Status Semantics

Helidon health endpoints use HTTP status to summarize the outcome of executing their selected checks. The source identifies successful responses as HTTP 200 or 204 and an unhealthy service response as HTTP 503 Service Unavailable.

The status allows infrastructure to make a decision without parsing the full JSON body, especially through a HEAD request. A GET response adds detailed check results while preserving the same overall operational meaning.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
