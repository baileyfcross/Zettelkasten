2026-10-03 16:51

Status: #baby

Tags: [[NVIDIA GPU Platform Operations]]

# NVIDIA Container Toolkit

The NVIDIA Container Toolkit connects a container runtime to NVIDIA devices and the compatible host driver. It makes GPU devices and required driver capabilities available inside a container while retaining the portability of the container's user-space environment.

Its role differs from the [[Kubernetes Device Plugin]], which advertises schedulable resources. A pod can be placed on a GPU node yet fail to see the device when runtime integration is missing, or runtime access can exist while the scheduler lacks an advertised resource.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

