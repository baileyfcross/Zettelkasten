2026-10-04 08:37

Status: #baby

Tags: [[Buildah Container Image Construction]], [[SLES Container and SAP Workload Operations]]

# Containerfile

A Containerfile is the vendor-neutral name for the instruction file used to build a container image. It uses the same syntax and semantics as a [[Dockerfile]], and Podman or Buildah can consume either filename without changing the build model.

Instructions are evaluated in order against a [[Build Context]]. `FROM` begins a stage, filesystem-changing instructions create layers, and configuration instructions record defaults such as the command, environment, user, working directory, or exposed ports. The alternate name removes branding, not compatibility.

SLES uses the Containerfile workflow with `podman build` to turn an application and its declared base image into a locally tagged image. Build inputs should be limited to the required context, and runtime data should remain outside the image so rebuilding does not become a persistence mechanism.

# References

[[podmanfordevopssecondedition.pdf]]
[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
