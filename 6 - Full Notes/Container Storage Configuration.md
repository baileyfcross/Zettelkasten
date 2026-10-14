2026-10-04 08:37

Status: #baby

Tags: [[Podman Container Lifecycle and Storage]] [[Docker Storage and Configuration]]

# Container Storage Configuration

Container storage configuration selects the graph driver and the persistent and runtime locations used for images, layers, containers, volumes, and transient metadata. In the containers/storage stack, `storage.conf` provides defaults and supports system-wide or per-user overrides.

The persistent graph root holds durable local image and container state, while the run root holds temporary data such as PID files and generated runtime mounts. Rootless and rootful Podman use different paths and ownership contexts, so copying a configuration between them without adjusting permissions and user-namespace behavior can make otherwise valid storage inaccessible.

Docker storage design should begin with the data's required lifetime and ownership. Writable layers suit disposable changes, tmpfs suits ephemeral memory-backed data, bind mounts suit intentionally host-coupled files, and named volumes suit Docker-managed persistence; none removes the need for backup and recovery design.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]

[[podmanfordevopssecondedition.pdf]]
