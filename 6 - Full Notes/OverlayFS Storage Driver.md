2026-10-04 08:37

Status: #baby

Tags: [[Podman Container Lifecycle and Storage]]

# OverlayFS Storage Driver

The OverlayFS storage driver combines read-only lower directories with a writable upper directory and presents them through one merged mount. Podman uses this union-filesystem behavior to share immutable image layers among containers while keeping each container's changes separate.

When a lower-layer file is changed, copy-on-write places the modified version in the upper layer; deletions are represented without rewriting the base image. The driver makes layered images efficient, but its paths are implementation storage rather than an application persistence interface. Administrators should use [[Container Storage Configuration]] and supported mounts instead of binding workloads to internal overlay directories.

# References

[[podmanfordevopssecondedition.pdf]]
