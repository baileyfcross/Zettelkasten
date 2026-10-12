2026-10-04 08:37

Status: #baby

Tags: [[Buildah Container Image Construction]]

# Containerized Buildah

Containerized Buildah runs the image builder inside a container so a CI system or Kubernetes workload can construct images without installing Buildah directly on the worker host. The builder still needs suitable storage and namespace behavior for creating nested build containers and writing image layers.

The book contrasts rootless volume-backed stores, bind-mounted stores, and native commands executed in the builder container. The design should grant only the mounts and capabilities the build requires; making the builder privileged for convenience weakens the isolation that containerizing the build was meant to provide.

# References

[[podmanfordevopssecondedition.pdf]]
