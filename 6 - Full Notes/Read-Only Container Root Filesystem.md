2026-10-11 21:26

Status: #baby

Tags: [[Docker Container Security]]

# Read-Only Container Root Filesystem

A read-only container root filesystem prevents the running process from modifying the image-derived filesystem. It reduces persistence opportunities after compromise and exposes applications that silently depend on writing into paths that were intended to be immutable.

Necessary writable locations should be mounted explicitly as narrow volumes or tmpfs paths for logs, temporary files, sockets, or uploads. This produces a reviewable write surface and preserves the image as the authoritative program state instead of allowing an instance to drift through undocumented runtime changes.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]
