2026-10-04 08:37

Status: #baby

Tags: [[Podman Workload Integration and Desktop]]

# Podman Docker CLI Compatibility

Podman Docker CLI compatibility keeps many command names, options, and workflows close enough to Docker that an alias or the `podman-docker` wrapper can redirect familiar `docker` invocations to Podman. Common image and container operations can therefore be tested with little script change.

Compatibility is an migration aid rather than proof of identical behavior. Daemon assumptions, unsupported subcommands, network defaults, rootless permissions, and Compose integration can differ. A migration should inventory its actual commands and observe workload behavior instead of treating a successful alias as complete validation.

# References

[[podmanfordevopssecondedition.pdf]]
