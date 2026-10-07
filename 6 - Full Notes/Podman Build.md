2026-10-04 08:37

Status: #baby

Tags: [[Buildah Container Image Construction]], [[SLES Container and SAP Workload Operations]]

# Podman Build

Podman build executes a Dockerfile or [[Containerfile]] to produce an OCI image. It pulls a missing base image, runs build instructions in temporary containers, commits filesystem-changing results as layers, records metadata instructions, and tags the completed image in local storage.

Podman vendors Buildah's build logic, so this familiar command is a convenient front end to the same underlying image-construction facilities. Intermediate layers can accelerate later builds through caching, but they also require pruning and deliberate [[Container Image Layer Optimization]] rather than assuming every cached object is waste.

On SLES, the command can build the book's application examples from a Containerfile and store the resulting image for later `podman run` operations. A successful build verifies construction, not runtime reachability, persistent storage, published ports, or the behavior of the application process.

# References

[[podmanfordevopssecondedition.pdf]]
[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
