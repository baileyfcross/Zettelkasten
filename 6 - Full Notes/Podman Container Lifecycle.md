2026-10-04 08:37

Status: #baby

Tags: [[Podman Container Lifecycle and Storage]], [[SLES Container and SAP Workload Operations]]

# Podman Container Lifecycle

The Podman container lifecycle separates creation, execution, suspension, stopping, restart, and removal. `podman create` prepares a container without starting its process; `start`, `pause`, `unpause`, `stop`, `restart`, and `rm` then move that named object through explicit states.

This separation matters operationally because a stopped container still retains configuration and its writable layer, while removal discards that ephemeral state. Durable application data belongs in a [[Container Named Volume]] or [[Container Bind Mount]], and repeatable configuration belongs in the image or runtime options rather than an ad hoc change inside the container.

SLES 16 presents Podman as its default container management tool and uses the same lifecycle distinction in administrative examples. Detached execution returns control to the shell while the container continues, so operators must use inspection, logs, and explicit stop or removal commands rather than equating the invoking command's exit with workload termination.

# References

[[podmanfordevopssecondedition.pdf]]
[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
