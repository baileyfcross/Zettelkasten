2026-09-29 22:24

Status: #baby

Tags: [[GenAI Resilience and Disaster Recovery]]

# Multi-Zone GenAI Inference

Multi-zone GenAI inference distributes model-serving replicas and compatible GPU nodes across independent availability zones. Topology spread constraints and disruption budgets keep a node or zone failure from removing every ready endpoint.

Availability depends on more than pod placement. Model storage, vector databases, ingress, identity, and network routing must also tolerate the lost zone, while cross-zone data transfer and scarce accelerator types can complicate an otherwise balanced topology.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

