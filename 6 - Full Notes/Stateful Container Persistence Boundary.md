2026-10-11 21:26

Status: #baby

Tags: [[Docker Storage and Configuration]]

# Stateful Container Persistence Boundary

A stateful container persistence boundary identifies which data belongs outside the disposable container instance. Database files, uploads, and durable application state cross that boundary into a volume or external storage, while caches and reproducible runtime files can remain ephemeral.

Selecting a persistent path is only the beginning. The design must also define ownership, backup and restore, consistency during snapshots, capacity monitoring, encryption, migration, and behavior when storage is unavailable. Replacing a container safely depends on those rules being independent of the container's writable layer.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]
