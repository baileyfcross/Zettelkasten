2026-09-27 11:23

Status: #baby

Tags: [[Containerized Microservice Architecture]] [[Buildah Container Image Construction]] [[Docker Image Engineering]]

# Multi-Stage Docker Build

A multi-stage Docker build uses one image with the .NET SDK to restore, compile, test, and publish an application, then copies only the published output into a separate runtime image. Build tools and intermediate files do not become part of the deployed container.

The result is smaller and has a narrower attack surface while retaining a reproducible build recipe. Stage ordering also affects cache reuse, so stable dependency inputs are commonly copied before frequently changing source files.

Buildah can reproduce this pattern either from multiple `FROM` stages in a Dockerfile or through native commands that create separate working containers and copy the finished artifact between them. The boundary between the builder and runtime stages is the important design decision; the particular front end used to express it is secondary.

A multi-stage Dockerfile separates compilation and packaging tools from the final runtime filesystem. Copying only the required artifacts into the last stage reduces image size and attack surface while keeping the complete build procedure reproducible in one file.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
[[podmanfordevopssecondedition.pdf]]
