2026-09-06 22:42

Status: #baby

Tags: [[Parallel Workload Resource Management]]

# Co-Scheduling

Co-scheduling runs several parallel applications at the same time and divides processors among them. A useful assignment exploits differing [[Application Speedup Profile|speedup profiles]] so the applications share capacity without unnecessarily extending the group's completion time.

For big-data workloads, alternating compute and I/O phases can create opportunities for one application to use resources another is not currently stressing.

# References

[[bigdatamanagementandprocessing.pdf]]
