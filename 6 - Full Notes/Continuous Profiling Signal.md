2026-10-03 17:11

Status: #baby

Tags: [[Observability Signals and Semantic Context]]

# Continuous Profiling Signal

A continuous profiling signal samples runtime execution to show where code spends processor time, allocates memory, or blocks. Unlike a request trace, which follows one transaction across services, a profile exposes repeated function- and stack-level behavior inside a process.

Profiles can connect a service-level slowdown to a hot code path or inefficient method, giving developers evidence for optimization. Because detailed stacks can be high-volume and sensitive, profiling depth, frequency, access, and retention need the same intentional design as other observability signals.

# References

[[observabilityintheai-nativeera.pdf]]
