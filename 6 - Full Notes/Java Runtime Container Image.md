2026-10-30 17:24

Status: #baby

Tags: [[Docker Image Engineering]]

# Java Runtime Container Image

A Java runtime container image contains the Java runtime and packaged application needed to start the service, while excluding the compiler and build tools used to create it. The image defines a repeatable execution environment that can run on a container host without a separate host JDK installation.

Keeping build and runtime concerns separate reduces image size and attack surface. Configuration, database state, and secrets should remain outside the immutable image so the same artifact can move across environments.

The source distinguishes a JDK base, which includes compilers and development tools, from a JRE-oriented base selected only to launch an already-built service. It also shows that the runtime distribution and operating-system variant are part of the deployment contract, leading to choices such as maintained OpenJDK, Eclipse Temurin, Alpine, or [[Distroless Java Container Image]].

# References

[[javamicroservicesandcontainersinthecloud.epub]]

[[whendockermeetsjava_apracticalguidetodockerforjavaandspringbootapp.epub]]

