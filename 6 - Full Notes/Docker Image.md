2026-09-08 22:09

Status: #baby

Tags: [[Containerized Microservice Architecture]]

# Docker Image

A Docker image is the packaged, versionable template used to start one or more containers. It contains the application layers and dependencies described by its Dockerfile but does not become a running process until a container is created from it.

The sales-order image is built locally, tested with `docker run`, tagged, and uploaded to a registry. Kubernetes then refers to that registered image when creating its worker pods.

# References

[[c8andnetcore30projectsusingazure.pdf]]
