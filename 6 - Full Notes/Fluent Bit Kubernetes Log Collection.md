2026-09-29 22:24

Status: #baby

Tags: [[GenAI Observability on Kubernetes]]

# Fluent Bit Kubernetes Log Collection

Fluent Bit Kubernetes log collection runs a lightweight agent as a DaemonSet or sidecar, reads container and node logs, enriches them with pod and namespace metadata, and forwards them to a central backend. Its small memory and CPU footprint suit dense clusters.

Collection policy should parse structured records, buffer temporary backend failure, and filter confidential prompt or credential data before export. Node coverage and rotation handling matter because a deleted model pod should not delete the only evidence of its behavior.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

