2026-09-29 22:24

Status: #baby

Tags: [[GenAI Resilience and Disaster Recovery]]

# Maximum Tolerable Downtime

Maximum tolerable downtime is the longest interval a service can remain unavailable before its consequences become unacceptable to the organization. It is an outer business-continuity limit rather than the engineered recovery target itself.

The [[Recovery Time Objective]] should fall inside this limit and leave margin for detection, decision-making, data validation, and resumption of dependent work. For a GenAI service, the limit should consider endpoint outage, retrieval and vector-store availability, and the time required to restore model artifacts onto accelerator capacity.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

