2026-10-30 17:24

Status: #baby

Tags: [[Docker Runtime and Container Lifecycle]]

# Containerization vs Hardware Virtualization

Hardware virtualization places a guest operating system and its libraries above a hypervisor for each virtual machine. Containerization instead isolates application processes while sharing the host kernel, packaging the application and its user-space dependencies without a complete guest operating system per instance.

Containers consequently start and replicate with less overhead, while virtual machines provide a stronger operating-system boundary and can run different kernels. Kubernetes orchestrates containers across nodes; it does not turn each container into a virtual machine.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

