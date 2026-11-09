2026-11-08 16:45

Status: #baby

Tags: [[Spring Cloud Operations and Native Runtime]]

# Spring Micrometer Business Metric

A Spring Micrometer business metric records application behavior through a meter registry independently of the eventual monitoring backend. A counter measures occurrences such as created customers, while a timer records count, total time, maximum, and configured latency percentiles for an operation.

Tags add bounded dimensions such as outcome, region, or customer type so a dashboard can group the measurement. Unbounded identifiers such as user or order IDs create high cardinality and can overwhelm the backend. Instrumentation should use stable names and stop timers in a finally path so failures are represented rather than disappearing from the duration series.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
