2026-10-14 00:45

Status: #baby

Tags: [[Windows Server Deployment and Administration]]

# Windows Server Hotpatching

Windows Server hotpatching applies supported operating-system updates to running processes without requiring an immediate reboot. It reduces update-related interruption for workloads whose availability makes frequent restarts costly, while still allowing security fixes to be deployed. Hotpatching is an update path, not a reason to abandon maintenance windows, compatibility testing, backups, or rollback planning.

For Windows Server 2025, the book's deployment model uses an [[Azure Arc-Enabled Server]] with an eligible Standard or Datacenter edition, Software Assurance, Virtualization-Based Security, and required prerequisite updates. A safe rollout inventories hardware and software dependencies, tests the patch in a production-like environment, records a performance baseline, applies the update in a controlled order, and validates services, logs, resource use, and security state afterward. Detailed monitoring and a rehearsed fallback path make a live update recoverable when compatibility or connectivity fails.

# References

[[windowsserver2025administrationfundamentals_fourthedition.pdf]]
