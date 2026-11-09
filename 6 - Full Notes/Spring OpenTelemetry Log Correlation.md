2026-11-08 16:45

Status: #baby

Tags: [[Spring Cloud Operations and Native Runtime]]

# Spring OpenTelemetry Log Correlation

Spring OpenTelemetry log correlation places the active trace identifier and span identifier into the logging context for work executed inside an instrumented request or observation. Ordinary SLF4J log records can then be grouped with the distributed trace that represents the same end-to-end transaction.

The trace ID connects records across services, while the span ID identifies the local operation that emitted a line. Correlation reduces the search needed to move from an error log to a trace, but it requires context propagation across every HTTP, messaging, and asynchronous boundary. The identifiers provide linkage, not permission to log sensitive payloads.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
