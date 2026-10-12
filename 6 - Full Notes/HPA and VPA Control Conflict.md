2026-09-29 22:24

Status: #baby

Tags: [[Kubernetes GenAI Autoscaling and Cost Control]]

# HPA and VPA Control Conflict

An HPA and VPA control conflict occurs when vertical automation changes the requests used as the baseline for horizontal utilization scaling. HPA may then interpret the same actual use as a different percentage and add or remove replicas in response to VPA's adjustment rather than a demand change.

The book recommends avoiding simultaneous automatic HPA and VPA control over the same resource dimension. VPA can remain in recommendation mode, or horizontal scaling can use a stable external metric that is not recalculated from requests.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

