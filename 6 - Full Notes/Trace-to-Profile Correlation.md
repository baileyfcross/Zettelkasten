2026-11-06 12:32

Status: #baby

Tags: [[Observability Signals and Semantic Context]]

# Trace-to-Profile Correlation

Trace-to-profile correlation uses a distributed trace to select the process, operation, and time interval that a profile should explain. The trace reveals which request segment was slow or failed; the profile then exposes call trees, stack traces, method counts, CPU time, allocations, memory behavior, and thread states that a span timeline cannot show.

This relationship keeps profiling targeted. Rather than searching an entire runtime for an unexplained hotspot, an investigator can begin with the service and interval identified by the trace and compare the method-level behavior with the span's latency and error context. The result distinguishes a slow dependency from work performed inside the process.

The two signals remain complementary: a [[Continuous Profiling Signal]] does not reconstruct an end-to-end request, and a [[Distributed Request Trace]] does not provide a full method or memory profile. Their shared process, thread, trace, and time context creates the useful diagnostic bridge.

# References

[[observabilityforlegacysystems_methodsandsolutionswithopentelemetry.epub]]
