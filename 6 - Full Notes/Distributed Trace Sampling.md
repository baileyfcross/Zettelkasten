2026-10-03 17:11

Status: #baby

Tags: [[Observability Signals and Semantic Context]]

# Distributed Trace Sampling

Distributed trace sampling chooses which request traces or spans are retained and which are discarded. It controls the cost and volume created by end-to-end instrumentation while preserving enough evidence to diagnose latency, errors, and dependency behavior.

A sampling strategy must account for rare failures and important transactions instead of merely keeping a fixed percentage. Over-instrumentation, duplicated data across traces and logs, and sampling that removes the exceptional request can all make a tracing system expensive yet diagnostically weak.

# References

[[observabilityintheai-nativeera.pdf]]
