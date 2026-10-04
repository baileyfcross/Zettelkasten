2026-10-04 08:37

Status: #baby

Tags: [[Podman Workload Integration and Desktop]]

# Quadlet Container Unit

A Quadlet container unit is a `.container` declaration from which the systemd generator creates a service that runs and supervises a Podman container. Its sections describe the image, name, environment, mounts, published ports, networks, dependencies, and service behavior without embedding a long `podman run` command in a handwritten unit.

Related Quadlet resource files can establish a managed volume or network before the container starts, and ordinary systemd directives can express ordering and restart policy. The generated `.service` is an implementation result; the `.container` file is the source that should be reviewed and versioned.

# References

[[podmanfordevopssecondedition.pdf]]
