2026-10-04 08:37

Status: #baby

Tags: [[Rootless Container and SELinux Security]] [[Docker Container Security]]

# Container Capability Set

A container capability set is the collection of [[Linux Capability]] values available to the container process. Podman starts from a default set and allows individual capabilities to be added or dropped so a workload receives specific kernel privileges without becoming fully privileged.

Least privilege starts by dropping what the application does not use and adding back only the operation that testing proves necessary. Capability control complements, rather than replaces, user namespaces, seccomp, read-only filesystems, and SELinux policy because each mechanism constrains a different route to host resources.

Linux capabilities split root's broad authority into smaller privileges that Docker can add or remove independently. A hardened container drops all capabilities and adds back only those proven necessary, combining that reduction with a non-root user, no-new-privileges, and a read-only root filesystem.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]

[[podmanfordevopssecondedition.pdf]]
