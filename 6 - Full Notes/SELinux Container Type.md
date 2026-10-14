2026-10-04 08:37

Status: #baby

Tags: [[Rootless Container and SELinux Security]]

# SELinux Container Type

An SELinux container type is the type label used by mandatory access-control policy to confine container processes and the objects they may access. A process may have ordinary Unix permission to open a host file and still be denied because the process type and file type are not allowed to interact.

Podman assigns container-aware labels and can relabel mounted content as shared or private. Multi-category labels further distinguish containers using the same general type, preventing one container from accessing another's files. Troubleshooting should examine the denial and intended access before disabling enforcement or applying a broad relabel.

# References

[[podmanfordevopssecondedition.pdf]]
