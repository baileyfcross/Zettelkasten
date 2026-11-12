2026-10-11 21:26

Status: #baby

Tags: [[Docker Runtime and Container Lifecycle]]

# Docker Engine REST Architecture

Docker Engine is the management layer above the container runtime. It coordinates image and container metadata, storage drivers, networking libraries, plugins, and lifecycle operations, then exposes those capabilities through a REST API. The Docker CLI and other clients translate user intent into calls to that API rather than performing isolation directly.

This separation makes the daemon endpoint a privileged control boundary. Anyone able to issue unrestricted Engine requests can create containers, mount host paths, or change network state, so socket access should be treated as administrative authority and limited independently from ordinary container permissions.

The book's build-tag-push sequence illustrates the same boundary: the CLI submits a build request, the daemon assembles the image from the Dockerfile and context, and later client requests assign a registry reference and publish the resulting layers. The command-line process coordinates those operations but does not itself become the image builder or container runtime.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]

[[whendockermeetsjava_apracticalguidetodockerforjavaandspringbootapp.epub]]
