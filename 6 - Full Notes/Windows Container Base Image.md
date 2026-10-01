2026-09-30 23:37

Status: #baby

Tags: [[Windows Server Virtualization and Containers]]

# Windows Container Base Image

A Windows container base image supplies the operating-system layer on which an application image is built. Nano Server offers the smallest footprint for compatible modern applications, Server Core includes a broader Windows API surface, and the Windows Server image supports still more traditional components at a larger size. The correct base is the smallest one that actually supports the workload.

Image layers make repeated builds and downloads efficient, but every layer becomes part of the artifact that must be patched and trusted. Updating a running container is normally accomplished by rebuilding from a newer base, testing the new image, and replacing instances rather than patching them individually. Base-image choice therefore affects compatibility, storage, startup, security surface, and the deployment pipeline throughout the application's life.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
