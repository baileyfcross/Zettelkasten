2026-11-06 12:32

Status: #baby

Tags: [[AIOps Incident Intelligence]]

# Root Cause Analysis Data Model

A root cause analysis data model joins the identifiers and observations needed to reconstruct a failure across business, application, and infrastructure layers. Its fields can include request, order, payment, transaction, trace, span, thread, system-trace, and system-span identifiers together with latency, error, release, entity, and resource context.

The trace acts as a central join path, but no single signal is complete. Events can connect business steps that generated separate traces, logs can fill gaps around a black box, profiles can reveal method and thread behavior, and [[System Trace Correlation]] can connect an application span to scheduling, network, disk, interrupt, or memory activity. The resulting structure supplies a common evidence base for anomalies, alerts, service objectives, configuration data, and a [[Root Cause Analysis Dashboard]].

When retained as an event-oriented history, the model also supports reproducibility: an investigator can revisit the evidence available during a past failure instead of relying only on a current dashboard state. That makes it a foundation for [[Root Cause Analysis]] and for AIOps explanations whose conclusions must remain traceable to observations.

# References

[[observabilityforlegacysystems_methodsandsolutionswithopentelemetry.epub]]
