2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Multitenancy and Secure Interfaces]]

# Highly Available vCluster

A highly available vCluster runs redundant virtual control-plane components and uses a data store capable of surviving a pod or node failure. This protects tenant API availability independently from the lifecycle of a single vCluster pod.

High availability still depends on the host cluster's failure domains, persistent storage, scheduling, and upgrade process. Replicas placed on one node or backed by one fragile volume provide the appearance of redundancy without eliminating the shared cause of failure.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

