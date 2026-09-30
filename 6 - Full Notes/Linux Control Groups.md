2026-09-30 01:38

Status: #baby

Tags: [[Linux CPU Scheduling and Control Groups]]

# Linux Control Groups

Linux control groups organize processes into a hierarchy for resource accounting, limits, protection, and allocation. Controllers govern resources such as CPU time, memory, process counts, and I/O without changing the process's namespace view.

Control groups complement the isolation used by a [[Linux Container]] but are independently useful for services and users. The unified [[Cgroup v2 Controller]] model coordinates multiple resources in one hierarchy that is commonly managed through the [[Systemd Cgroup Hierarchy]].

# References

[[linuxkernelprogramming_secondedition.pdf]]
