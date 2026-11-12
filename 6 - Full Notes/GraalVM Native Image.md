2026-11-11 19:33

Status: #baby

Tags: [[Java Low-Level Platform and Native Performance]]

# GraalVM Native Image

A GraalVM native image is a platform-specific executable produced ahead of time from Java bytecode, application classes, dependencies, and required runtime code. It trades the ordinary JVM startup path for a precompiled application artifact intended to start quickly and use less memory.

A native image and a container image solve different problems. Native-image compilation specializes the Java program for a target platform, whereas a container image packages a filesystem and startup contract for a container runtime. A native executable can be placed inside a container, as in a [[Spring Boot Native Image Build]], but neither artifact is a substitute for the other.

# References

[[whendockermeetsjava_apracticalguidetodockerforjavaandspringbootapp.epub]]
