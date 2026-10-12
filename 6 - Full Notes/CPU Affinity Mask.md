2026-09-30 01:38

Status: #baby

Tags: [[Linux CPU Scheduling and Control Groups]]

# CPU Affinity Mask

A CPU affinity mask defines the processors on which a task is eligible to run. Restricting the mask can preserve cache locality, isolate latency-sensitive work, honor hardware constraints, or align computation with nearby [[NUMA Affinity]] memory.

Affinity narrows the choices available to scheduler load balancing and can reduce utilization when constrained too tightly. The effective set also intersects with online CPUs and control-group restrictions, so a requested mask may not be the only limit on placement.

# References

[[linuxkernelprogramming_secondedition.pdf]]
