2026-10-03 17:11

Status: #baby

Tags: [[AIOps Incident Intelligence]]

# Observability Data Quality for AIOps

Observability data quality is the degree to which telemetry is accurate, structured, timely, appropriately sampled, and enriched with enough context to support a decision. Useful context identifies origin, environment, version, ownership, dependencies, and the change events that may explain a behavior.

Enrichment is most efficient near the source or in a controlled collection pipeline. AI cannot reconstruct metadata that was never captured, and large quantities of context-free data increase storage and analysis cost while still leaving root-cause conclusions ambiguous.

The book describes the concrete failure modes behind poor quality: joins that do not resolve, missing or duplicated identifiers, broken propagation, unclear semantics, absent relationships, and signals stored in incompatible structures. AIOps cannot repair those defects by adding a model. A [[Root Cause Analysis Data Model]] and explicit correlation checks must first organize business identifiers, entities, signals, releases, and system context into evidence that can be searched and reproduced.

# References

[[observabilityintheai-nativeera.pdf]]
[[observabilityforlegacysystems_methodsandsolutionswithopentelemetry.epub]]
