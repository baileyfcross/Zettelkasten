2026-10-04 08:37

Status: #baby

Tags: [[Podman Workload Integration and Desktop]]

# Podlet

Podlet is a translation utility that converts Podman command lines, Compose definitions, or related container configuration into [[Quadlet]] files. It helps preserve image, mount, port, environment, and other run options while changing from an imperative launch command to declarative systemd management.

Generated output is a migration aid, not a finished service design. The operator should review naming, dependencies, secrets, restart behavior, installation path, user versus system scope, and systemd enablement before relying on the unit in production.

# References

[[podmanfordevopssecondedition.pdf]]
