2026-09-22 20:53

Status: #baby

Tags: [[Event Sourcing and Projections]]

# Projection Checkpoint

A projection checkpoint records the last event-stream position successfully applied to a [[Read Model]]. On restart, the [[Projection]] resumes after this position instead of replaying all history. Updating the checkpoint only after the read-side update provides at-least-once processing, so handlers must account for possible duplicates. Keeping the checkpoint in the same storage and transaction as the read model makes their progress consistent and allows both to be discarded together for a clean rebuild.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
