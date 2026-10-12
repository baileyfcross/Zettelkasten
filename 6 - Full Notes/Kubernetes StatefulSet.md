2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Cluster Architecture and Resources]]

# Kubernetes StatefulSet

A StatefulSet manages pods that need stable ordinal identities, ordered creation or termination, or persistent storage associated with a particular replica. Unlike interchangeable Deployment pods, its members receive predictable names and can retain distinct volume claims across replacement.

Stable identity does not make the pod itself durable. The workload must still place lasting data in persistent volumes or external stores, and its application-level replication must tolerate node and zone failures. StatefulSet provides lifecycle structure, not an automatic database recovery strategy.

The controller's ordered identities make peer discovery and per-replica volume claims predictable, but they can also serialize rollout and recovery. A StatefulSet should therefore be selected for identity or ordering requirements, not merely because an application writes data.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]

[[kubernetes_anenterpriseguidethirdedition.pdf]]

