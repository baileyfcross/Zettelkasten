2026-09-06 22:42

Status: #baby

Tags: [[Data Center Storage Networking]] [[Linux CPU Scheduling and Control Groups]]

# NUMA Affinity

NUMA affinity places a thread and the memory or device queues it frequently accesses on the same non-uniform memory access node. Local placement avoids cross-socket transfers with higher latency and shared interconnect cost.

For a high-rate storage path, interrupt handling, buffers, worker threads, and network interfaces should be assigned with the machine's memory topology in mind.

Linux expresses eligible processors through a [[CPU Affinity Mask]]. Keeping a task near its allocated NUMA node can reduce remote memory traffic, but scheduler load balancing, cpusets, and changing workloads mean that pinning should preserve enough placement flexibility to avoid creating idle CPUs beside overloaded ones.

# References

[[bigdatamanagementandprocessing.pdf]]
[[linuxkernelprogramming_secondedition.pdf]]
