2026-10-04 08:37

Status: #baby

Tags: [[Buildah Container Image Construction]]

# Scratch Container Image

A scratch container image begins without a parent filesystem layer. The builder adds only the application and the precise runtime files it needs, then supplies image configuration such as the command, working directory, ports, and non-root user.

This can create a very small artifact and avoid inheriting unused packages, but the application must be self-contained enough to run without an ordinary distribution userland. Missing certificates, libraries, identity files, shells, and diagnostic tools become design decisions rather than accidental defaults, which also affects later [[nsenter Container Debugging]].

# References

[[podmanfordevopssecondedition.pdf]]
