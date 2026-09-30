2026-09-30 01:38

Status: #baby

Tags: [[Linux CPU Scheduling and Control Groups]]

# Systemd Cgroup Hierarchy

The systemd cgroup hierarchy maps service units, scopes, and slices onto [[Linux Control Groups]]. Services receive managed groups for their processes, scopes represent externally created groups, and slices provide hierarchical resource organization for sets of units.

This integration makes process supervision and resource policy use the same ownership structure. Administrators normally configure unit resource properties through systemd rather than moving service processes manually, allowing the manager to preserve the hierarchy across restarts and lifecycle changes.

# References

[[linuxkernelprogramming_secondedition.pdf]]
