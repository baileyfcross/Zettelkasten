2026-09-30 01:38

Status: #baby

Tags: [[Linux CPU Scheduling and Control Groups]] [[Docker Runtime and Container Lifecycle]]

# Cgroup v2 Controller

A cgroup v2 controller applies a particular resource policy within the unified Linux control-group hierarchy. Controllers expose files for configuration and statistics, and their availability is delegated downward from parent groups according to explicit hierarchy rules.

The unified design makes resource distribution composable and avoids many inconsistencies of multiple independent v1 hierarchies. Internal-process and delegation constraints preserve a meaningful tree in which child groups subdivide resources made available by their parent.

Docker uses control groups to meter and limit a container's CPU, memory, and other resource consumption independently of namespace isolation. Explicit limits turn host capacity into an enforceable boundary and reduce the chance that one workload degrades every other container on the node.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]

[[linuxkernelprogramming_secondedition.pdf]]
