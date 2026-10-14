2026-10-11 21:26

Status: #baby

Tags: [[Docker Image Engineering]]

# Docker Image Save and Load

Docker image save exports one or more local images, including their layer and tag metadata, into a tar archive. Docker image load imports that archive back into a local image store, which is useful for backup, transfer into a disconnected environment, or movement where a registry is unavailable.

The archive is a transport form, not a new trust boundary. Its contents still need controlled provenance, integrity verification, vulnerability review, and an unambiguous image identity before deployment. Exporting an image also differs from exporting a container filesystem because image save preserves image structure rather than one instance's writable state.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]
