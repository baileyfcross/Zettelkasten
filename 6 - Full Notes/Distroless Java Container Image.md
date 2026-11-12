2026-11-11 19:33

Status: #baby

Tags: [[Docker Image Engineering]] [[Docker Container Security]]

# Distroless Java Container Image

A distroless Java container image retains the Java runtime components needed by the application while omitting the shell, package manager, and other general-purpose operating-system utilities. Removing those unused facilities produces a smaller runtime artifact and narrows the software available to an attacker.

This image is a runtime choice, not a build environment. Compilation and packaging can occur in a fuller JDK stage, after which a [[Multi-Stage Docker Build]] copies the finished application into the distroless base. The resulting container should start the Java application directly because interactive shell-based administration is not part of the image.

# References

[[whendockermeetsjava_apracticalguidetodockerforjavaandspringbootapp.epub]]
