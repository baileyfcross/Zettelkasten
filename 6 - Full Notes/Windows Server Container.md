2026-09-30 23:37

Status: #baby

Tags: [[Windows Server Virtualization and Containers]]

# Windows Server Container

A Windows Server container uses process isolation, sharing the host kernel while isolating the container's processes, filesystem, registry, and networking view. The shared kernel makes instances lighter and faster to start than full virtual machines, allowing more application units on one host.

That efficiency creates a compatibility and trust boundary. The container base image must align with the host's supported Windows version, and kernel sharing makes process isolation best suited to workloads within an accepted trust level. Resource controls and namespaces reduce interference but do not turn the container into a separate operating system. When tenants are less trusted or host-version flexibility matters, a [[Hyper-V Container]] can supply a stronger kernel boundary at additional cost.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
