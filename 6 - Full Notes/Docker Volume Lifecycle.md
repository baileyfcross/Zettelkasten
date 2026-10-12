2026-10-11 21:26

Status: #baby

Tags: [[Docker Storage and Configuration]]

# Docker Volume Lifecycle

A Docker volume has a lifecycle independent of any one container. It can be created explicitly or on demand, mounted by successive containers, inspected, backed up, and removed after the workload no longer needs its data. Removing a container therefore does not imply that its named volume should be deleted.

This independence prevents accidental loss during instance replacement but also creates orphaned storage and stale sensitive data when ownership is unclear. Cleanup commands should treat volumes more cautiously than disposable containers and images, and production volumes need capacity, backup, restore, permission, and encryption policies of their own.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]
