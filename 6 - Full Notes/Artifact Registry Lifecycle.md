2026-10-03 22:25

Status: #baby

Tags: [[Platform Delivery and Artifact Automation]]

# Artifact Registry Lifecycle

The artifact registry lifecycle spans upload, scanning, replication, download, promotion, retention, and deletion. Registry webhooks can turn each transition into a [[Software Lifecycle Event]], allowing security, deployment, storage, and audit systems to respond without polling.

Lifecycle policy must balance reproducibility with storage cost. Immutable released versions prevent silent replacement, scheduled rescanning finds vulnerabilities disclosed after upload, and retention rules remove unneeded artifacts without destroying versions still referenced by an environment or recovery plan. Deletion should therefore depend on live release inventory rather than age alone.

# References

[[platformengineeringforarchitects.pdf]]
