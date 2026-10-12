2026-09-27 22:21

Status: #baby

Tags: [[Azure Kubernetes Service Operations]]

# Kubernetes Reconciliation Loop

A Kubernetes reconciliation loop repeatedly compares the desired state declared for an object with the actual state observed in the cluster. When a deployment requests three replicas and only two healthy pods exist, its controller creates another pod to close the difference.

This loop is the mechanism behind [[Kubernetes Self-Healing]]. Desired state remains authoritative while individual pods are replaceable. Reconciliation also means operators should change declarations rather than relying on an unrecorded manual repair that a controller may later reverse.

# References

[[clouddevopsengineersguide.pdf]]

