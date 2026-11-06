2026-11-06 12:32

Status: #baby

Tags: [[Observability Signals and Semantic Context]]

# Business-to-System Correlation Chain

A business-to-system correlation chain links a user or business transaction to progressively lower-level execution identifiers. A session can contain several actions; an action can carry a request, order, payment, or transaction identifier; each step can produce one or more trace and span identifiers; and a span can be related to process, thread, system-trace, and system-span identifiers.

The chain is needed because a trace identifier is technical rather than end-to-end from the user's perspective. An order may require several clicks and therefore several traces, while asynchronous middleware or a black box may break an otherwise continuous parent-child path. A stable business identifier lets a [[Root Cause Analysis Dashboard]] reconstruct those traces chronologically and connect them to [[System Trace Correlation|system activity]].

Identifier design is part of the data model rather than an ad hoc logging choice. Names, propagation rules, storage, access, and privacy must be consistent enough for joins while avoiding exposure of sensitive message payloads.

# References

[[observabilityforlegacysystems_methodsandsolutionswithopentelemetry.epub]]
