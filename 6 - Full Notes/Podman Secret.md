2026-10-04 08:37

Status: #baby

Tags: [[Podman Workload Integration and Desktop]]

# Podman Secret

A Podman secret is a named value stored by a configured secret driver and mounted or exposed to a container at runtime instead of being baked into its image. This separates a workload declaration from the credential value and lets Quadlet-managed containers refer to the name.

The book's default file-driver example protects its store with filesystem permissions but keeps the value only Base64-encoded, not encrypted. A Podman secret therefore improves delivery and reduces accidental image exposure, yet its storage driver, host access, rotation, backup, and logging behavior still determine whether it is adequately protected.

# References

[[podmanfordevopssecondedition.pdf]]
