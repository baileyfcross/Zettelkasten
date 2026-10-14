2026-10-03 16:51

Status: #baby

Tags: [[GPU Virtualization and DPU Offload]]

# vGPU Scheduling Policy

A vGPU scheduling policy controls how processing time on a shared physical GPU is distributed among virtual machines. The source describes best-effort, equal-share, and fixed-share policies on supported configurations, along with time-slice choices that trade responsiveness against switching overhead and throughput.

Scheduling policy complements memory and capability profiles. A workload can have an adequate framebuffer allocation yet receive unpredictable compute service if contention and the chosen policy do not match its latency or fairness requirements.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

