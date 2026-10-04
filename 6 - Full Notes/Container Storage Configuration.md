2026-10-04 08:37

Status: #baby

Tags: [[Podman Container Lifecycle and Storage]]

# Container Storage Configuration

Container storage configuration selects the graph driver and the persistent and runtime locations used for images, layers, containers, volumes, and transient metadata. In the containers/storage stack, `storage.conf` provides defaults and supports system-wide or per-user overrides.

The persistent graph root holds durable local image and container state, while the run root holds temporary data such as PID files and generated runtime mounts. Rootless and rootful Podman use different paths and ownership contexts, so copying a configuration between them without adjusting permissions and user-namespace behavior can make otherwise valid storage inaccessible.

# References

[[podmanfordevopssecondedition.pdf]]
