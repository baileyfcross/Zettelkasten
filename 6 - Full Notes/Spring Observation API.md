2026-11-08 16:45

Status: #baby

Tags: [[Spring Cloud Operations and Native Runtime]]

# Spring Observation API

The Spring Observation API wraps one operation in a lifecycle that can produce both a Micrometer timing measurement and an OpenTelemetry span. An observation registry places the operation in scope, records errors, and stops it after the observed code completes.

This gives custom business work the same context model as automatically instrumented HTTP or database operations. Observation handlers can add a bounded attribute such as deployment region to every matching observation. The API unifies instrumentation, but exporters and backend routing remain deployment concerns handled by [[OpenTelemetry Trace Instrumentation]] and metric registries.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
