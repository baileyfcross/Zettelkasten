2026-10-04 08:37

Status: #baby

Tags: [[Rootless Container and SELinux Security]]

# Container Capability Set

A container capability set is the collection of [[Linux Capability]] values available to the container process. Podman starts from a default set and allows individual capabilities to be added or dropped so a workload receives specific kernel privileges without becoming fully privileged.

Least privilege starts by dropping what the application does not use and adding back only the operation that testing proves necessary. Capability control complements, rather than replaces, user namespaces, seccomp, read-only filesystems, and SELinux policy because each mechanism constrains a different route to host resources.

# References

[[podmanfordevopssecondedition.pdf]]
