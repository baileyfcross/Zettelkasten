2026-09-30 01:38

Status: #baby

Tags: [[Linux CPU Scheduling and Control Groups]] [[Podman Runtime Architecture and Isolation]]

# Linux Control Groups

Linux control groups organize processes into a hierarchy for resource accounting, limits, protection, and allocation. Controllers govern resources such as CPU time, memory, process counts, and I/O without changing the process's namespace view.

Control groups complement the isolation used by a [[Linux Container]] but are independently useful for services and users. The unified [[Cgroup v2 Controller]] model coordinates multiple resources in one hierarchy that is commonly managed through the [[Systemd Cgroup Hierarchy]].

Container engines use this mechanism separately from namespaces: namespaces change the resources a process can see, whereas cgroups account for and constrain how much CPU, memory, I/O, or other controlled resources the process may consume. The book emphasizes cgroup v2's unified hierarchy as the modern basis for container resource control.

# References

[[linuxkernelprogramming_secondedition.pdf]]
[[podmanfordevopssecondedition.pdf]]
