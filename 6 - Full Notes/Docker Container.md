2026-09-08 22:09

Status: #baby

Tags: [[Containerized Microservice Architecture]]

# Docker Container

A Docker container is an isolated running instance created from an image that packages an application and its dependencies. It avoids relying on a target machine to reproduce the exact library and framework environment used during development and testing.

The book runs its .NET Core 3 worker in a Linux container. The container is lighter than copying an entire virtual machine because it packages the application environment while remaining abstracted from much of the host operating system.

# References

[[c8andnetcore30projectsusingazure.pdf]]
