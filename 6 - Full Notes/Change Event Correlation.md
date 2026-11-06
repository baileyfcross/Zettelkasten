2026-10-03 17:11

Status: #baby

Tags: [[AIOps Incident Intelligence]]

# Change Event Correlation

Change event correlation compares an abnormal behavior with deployments, configuration updates, feature-flag changes, pipeline runs, and other lifecycle events in the same period. It can reveal that a new resource limit, release, or routing rule preceded the symptom.

Temporal proximity is evidence rather than proof. The analysis must also establish that the changed component lies on the affected dependency path and that the observed mechanism can explain the impact. This prevents every recent release from becoming the default suspect.

The current source illustrates this with a memory increase and repeated full collections that began after an instrumentation patch. Garbage collection and latency are effects; the deployment becomes a stronger causal candidate only when the timeline, affected JVM generation, component path, and profile support the mechanism. Recording release context inside the RCA evidence model makes that distinction testable.

# References

[[observabilityintheai-nativeera.pdf]]
[[observabilityforlegacysystems_methodsandsolutionswithopentelemetry.epub]]
