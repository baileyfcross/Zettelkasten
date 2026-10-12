2026-09-08 22:09

Status: #baby

Tags: [[Containerized Microservice Architecture]] [[Docker Runtime and Container Lifecycle]]

# Docker Container

A Docker container is an isolated running instance created from an image that packages an application and its dependencies. It avoids relying on a target machine to reproduce the exact library and framework environment used during development and testing.

The book runs its .NET Core 3 worker in a Linux container. The container is lighter than copying an entire virtual machine because it packages the application environment while remaining abstracted from much of the host operating system.

For microservice deployment, the container supplies an isolated, repeatable runtime unit across compatible hosts. The book connects that packaging boundary to independent service deployment while keeping durable state and service contracts outside the disposable container instance.

Docker implements this unit as an ordinary host process whose view of processes, networking, mounts, and other resources is restricted by Linux namespaces. Resource controls such as cgroups complement that isolation, while the image supplies a repeatable filesystem and a thin writable layer records runtime changes.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]

[[c8andnetcore30projectsusingazure.pdf]]
[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
