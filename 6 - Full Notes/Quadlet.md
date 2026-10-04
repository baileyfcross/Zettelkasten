2026-10-04 08:37

Status: #baby

Tags: [[Podman Workload Integration and Desktop]]

# Quadlet

Quadlet is Podman's declarative integration with systemd. Files describing containers, pods, volumes, networks, images, and related resources are read by a systemd generator, which produces ordinary service units at load time using the current Podman implementation.

This replaces the brittle practice of generating a static service file once and forgetting to regenerate it as recommended unit behavior changes. Quadlet keeps the container intent concise while systemd provides dependency ordering, startup, restart, enablement, logs, and service lifecycle. [[Podlet]] can translate an existing run command into a useful starting file.

# References

[[podmanfordevopssecondedition.pdf]]
