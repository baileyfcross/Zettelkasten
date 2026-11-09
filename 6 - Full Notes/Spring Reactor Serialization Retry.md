2026-11-08 16:45

Status: #baby

Tags: [[Spring Web and Service Interfaces]]

# Spring Reactor Serialization Retry

A Spring Reactor serialization retry resubscribes to a reactive database operation when the driver reports a retryable transaction conflict. The retry filter should recognize the serialization-failure SQL state, and exponential backoff gives a competing transaction time to finish before the next attempt.

Filtering is essential: validation, authorization, and permanent query errors should fail immediately rather than be repeated. The retry remains inside the `Mono` or `Flux` pipeline, preserving nonblocking execution, and exhaustion needs a defined error response or durable recovery path. This is the reactive counterpart to a proxy-based imperative retry around distributed SQL work.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
