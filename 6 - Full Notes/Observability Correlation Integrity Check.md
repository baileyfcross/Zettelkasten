2026-11-06 12:32

Status: #baby

Tags: [[Observability Signals and Semantic Context]]

# Observability Correlation Integrity Check

An observability correlation integrity check tests whether the expected navigation between signals actually works. A responder should be able to move from a metric or real-user symptom to a trace, from the trace to logs and profiles, and from an application span to the related infrastructure evidence using shared identifiers and entity context.

A failed join is not merely a dashboard inconvenience. It can reveal missing instrumentation, an incorrectly propagated trace context, absent identifiers in logs, incompatible agent formats, clock or entity mismatches, or a collection gap. These faults reduce the quality of every downstream alert, dashboard, anomaly detector, and AIOps conclusion.

The check turns [[Observability Signal Correlation]] into a testable contract. Representative transactions can verify that trace, span, thread, business, and resource identifiers survive the intended path and that each stored signal can be reached from the others without manual guesswork.

# References

[[observabilityforlegacysystems_methodsandsolutionswithopentelemetry.epub]]
