2026-09-22 20:53

Status: #baby

Tags: [[Event Sourcing and Projections]]

# Projection

A projection transforms domain events into a [[Read Model]]. It subscribes to one or more streams, handles the event types relevant to its view, and inserts, updates, or removes read-side records. Because event streams are optimized for aggregate history rather than filtering current state, projections create representations suited to queries. A projection must tolerate restart and repeated delivery, advance its [[Projection Checkpoint]] only after successful processing, and be rebuildable through replay where practical.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
