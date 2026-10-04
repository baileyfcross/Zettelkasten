2026-10-04 08:37

Status: #baby

Tags: [[Podman Container Lifecycle and Storage]]

# Container Bind Mount

A container bind mount exposes an existing host file or directory at a chosen path inside the container. The host controls the source's location, contents, permissions, and lifecycle, while Podman configures the mount through compact `-v` syntax or the more explicit `--mount type=bind` form.

Bind mounts are useful when an application must see host-managed configuration or data, but they couple the workload to that host path and hide any image content already present at the destination. On SELinux systems, the source may also require an appropriate shared or private relabel; careless relabeling of system directories can disrupt host processes.

# References

[[podmanfordevopssecondedition.pdf]]
