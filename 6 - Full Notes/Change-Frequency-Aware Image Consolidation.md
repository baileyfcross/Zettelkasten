2026-09-28 04:01

Status: #baby

Tags: [[Image Request Consolidation]]

# Change-Frequency-Aware Image Consolidation

Assets grouped into one consolidated resource share an invalidation boundary. Changing one member changes the sprite or bundle URL and can force clients to fetch all members again.

Grouping should therefore reflect how often assets change and how often they are used together. Stable global icons belong in a different bundle from frequently revised campaign graphics. This preserves request savings without turning a small update into a large cache miss.

# References

[[highperformanceimages.pdf]]
