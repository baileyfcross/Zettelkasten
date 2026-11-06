2026-11-06 12:32

Status: #baby

Tags: [[AIOps Incident Intelligence]]

# Root Cause Analysis Escalation Ladder

A root cause analysis escalation ladder moves from broad, inexpensive evidence toward increasingly detailed and costly evidence. Metrics and service objectives first narrow the problem area; a [[Distributed Request Trace]] and [[Continuous Profiling Signal|profile]] then locate the affected request, method, thread state, or allocation behavior; [[System Trace Correlation]] and kernel-level profiling are reserved for delays that application evidence cannot explain.

The order protects both response time and analytical depth. A resource-setting mistake may be resolved from metrics, while a slow dependency may require spans and a method profile. Recurring contention, interrupts, retransmission, scheduling delay, or memory activity may justify system traces and eBPF evidence because stopping at the application symptom would leave the underlying condition in place.

The ladder is not a claim that one signal is universally superior. It is a disciplined way to choose the next source of evidence in [[Root Cause Analysis]] while avoiding a jump from a high-level symptom directly to an expensive low-level investigation.

# References

[[observabilityforlegacysystems_methodsandsolutionswithopentelemetry.epub]]
