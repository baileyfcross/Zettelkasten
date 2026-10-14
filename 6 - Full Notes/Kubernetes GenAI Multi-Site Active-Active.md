2026-09-29 22:24

Status: #baby

Tags: [[GenAI Resilience and Disaster Recovery]]

# Kubernetes GenAI Multi-Site Active-Active

Kubernetes GenAI multi-site active-active runs serving workloads and replicated data in more than one cluster or region while directing live traffic to each site. Health-aware global routing can remove a failed site without waiting to create its replacement environment.

The design offers the shortest recovery and smallest data-loss window at the highest cost and complexity. Model-version synchronization, vector and application data consistency, prompt routing, accelerator capacity, and failover semantics must remain coordinated across sites.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

