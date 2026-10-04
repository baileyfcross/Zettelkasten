2026-10-04 08:37

Status: #baby

Tags: [[Podman Container Lifecycle and Storage]]

# Container Exec

Container exec starts an additional process inside the namespaces and filesystem of an already running container. With Podman it is useful for a targeted command, inspection, or short interactive session without replacing the container's main process.

The command can run only a binary present in the container image, which limits its usefulness with minimal images that omit shells and diagnostic tools. [[nsenter Container Debugging]] can instead join the container's namespaces from the host and use host-installed tools, preserving the small production image while enabling deeper investigation.

# References

[[podmanfordevopssecondedition.pdf]]
