2026-10-03 17:11

Status: #baby

Tags: [[Observability Signals and Semantic Context]]

# Continuous Profiling Signal

A continuous profiling signal samples runtime execution to show where code spends processor time, allocates memory, or blocks. Unlike a request trace, which follows one transaction across services, a profile exposes repeated function- and stack-level behavior inside a process.

Profiles can connect a service-level slowdown to a hot code path or inefficient method, giving developers evidence for optimization. Because detailed stacks can be high-volume and sensitive, profiling depth, frequency, access, and retention need the same intentional design as other observability signals.

The book uses [[Trace-to-Profile Correlation]] to make that evidence operational. A trace selects the affected service, request, and interval, after which a profile can expose method counts, self and total CPU time, call relationships, thread states, memory behavior, or an inbound and outbound method hidden inside a black box. Profiling is thus a method-level complement to the request timeline rather than a replacement for it.

# References

[[observabilityintheai-nativeera.pdf]]
[[observabilityforlegacysystems_methodsandsolutionswithopentelemetry.epub]]
