2026-09-30 23:37

Status: #baby

Tags: [[Windows Server Virtualization and Containers]]

# Hyper-V Role

The Hyper-V role turns Windows Server into a type-1 virtualization host that runs isolated virtual machines through the Windows hypervisor. Each VM receives virtual processors, memory, firmware, disks, and network adapters, while the management operating system controls the host and exposes Hyper-V administration tools.

Host design begins with hardware virtualization support, capacity, storage, and network paths rather than with the New Virtual Machine wizard. Production hosts should reserve resources for the management partition, separate or protect traffic classes, and avoid unrelated roles that compete with tenant workloads. Clustering can restart or live-migrate VMs across hosts, but availability depends on shared or replicated storage, compatible networking, and consistent virtual-switch definitions as well as the Hyper-V role itself.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
