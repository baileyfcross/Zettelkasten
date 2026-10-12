2026-10-04 08:37

Status: #baby

Tags: [[Podman Runtime Architecture and Isolation]] [[Docker Runtime and Container Lifecycle]]

# Linux Namespace Isolation

Linux namespaces make selected system resources appear private to a process group. Mount, PID, user, UTS, network, IPC, cgroup, and time namespaces isolate different views, so two processes can have distinct filesystems, process-number spaces, identities, hostnames, network stacks, communication objects, cgroup paths, or clock offsets while sharing one kernel.

Namespaces are composable rather than all-or-nothing. A process created with only a PID namespace may see itself as PID 1 while still sharing the host network; adding a network namespace changes that view independently. Container runtimes turn this low-level combination into reproducible [[Container Process Isolation]].

Docker combines several namespaces so a container receives restricted views of process identifiers, networking, mounts, host names, users, and interprocess communication. This is isolation through kernel-scoped views, not a separate guest kernel, which explains both containers' low overhead and the importance of host-kernel security.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]

[[podmanfordevopssecondedition.pdf]]
