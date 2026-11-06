2026-11-06 12:32

Status: #baby

Tags: [[Observability Signals and Semantic Context]]

# System Trace Correlation

System trace correlation connects a distributed application span to the operating-system activity that executed it. Process identifiers, thread identifiers, file descriptors, timestamps, and explicit markers can associate a request with system calls, scheduling, context switches, interrupts, disk activity, memory allocation, packet retransmission, and other low-level events.

The correlation fills a gap between application and infrastructure evidence. A distributed trace can locate a slow service segment, while a system trace can show whether that interval contained waiting, contention, congestion, interference, or resource activity. Kernel profiling can then aggregate the implicated methods when the chronological system trace does not explain their frequency or tail latency.

Non-blocking execution and thread changes make a thread identifier insufficient by itself, so the source recommends preserving business and trace identifiers alongside process and thread context. The combined path supports the final stage of a [[Root Cause Analysis Escalation Ladder]] without pretending that one tracing tool contains every necessary view.

# References

[[observabilityforlegacysystems_methodsandsolutionswithopentelemetry.epub]]
