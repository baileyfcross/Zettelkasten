2026-10-04 08:37

Status: #baby

Tags: [[Podman Container Lifecycle and Storage]]

# Container Named Volume

A container named volume is a storage directory whose creation, location, and lifecycle are managed by the container engine and referenced by a stable name. Podman mounts it at a container path, preserves it after the container is removed, and lets later containers reuse the same data.

Unlike a [[Container Bind Mount]], a volume does not require the workload definition to know an arbitrary host directory. An empty new volume can be populated from the destination's existing image content, while a pre-populated volume obscures that content when mounted. Volumes persist independently and therefore need their own inspection, backup, and pruning policy.

# References

[[podmanfordevopssecondedition.pdf]]
