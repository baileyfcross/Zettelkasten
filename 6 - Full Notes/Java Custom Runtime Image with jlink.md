2026-11-11 19:33

Status: #baby

Tags: [[Java Platform Runtime and Project Structure]] [[Docker Image Engineering]]

# Java Custom Runtime Image with jlink

The Java `jlink` tool creates a self-contained runtime image containing only the Java platform and application modules selected for one deployment. `jdeps` can identify module dependencies, after which `jlink` receives the module path, required modules, compression choices, and output directory.

This applies the [[Java Platform Module System]] to deployment size and attack surface rather than source organization alone. In a container build, a JDK stage can compile the application and create the tailored runtime, then a [[Multi-Stage Docker Build]] copies that runtime and the application into a minimal final image. The target host does not need a separate full Java installation.

# References

[[whendockermeetsjava_apracticalguidetodockerforjavaandspringbootapp.epub]]
