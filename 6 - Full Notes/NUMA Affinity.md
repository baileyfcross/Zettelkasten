2026-09-06 22:42

Status: #baby

Tags: [[Data Center Storage Networking]]

# NUMA Affinity

NUMA affinity places a thread and the memory or device queues it frequently accesses on the same non-uniform memory access node. Local placement avoids cross-socket transfers with higher latency and shared interconnect cost.

For a high-rate storage path, interrupt handling, buffers, worker threads, and network interfaces should be assigned with the machine's memory topology in mind.

# References

[[bigdatamanagementandprocessing.pdf]]
