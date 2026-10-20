2026-10-19 22:48

Status: #baby

Tags: [[Helidon Platform Models and Project Tooling]]

# Helidon GraalVM Native Image Packaging

Helidon project templates include a native-image configuration area and a `Dockerfile.native` route for building a container that runs a GraalVM native executable. This converts the Java application ahead of time instead of requiring the ordinary packaged JAR and full JVM startup path.

Helidon SE supported GraalVM early in the framework's history, while Helidon MP gained native-image support after its reflection-related limitation was addressed. Native packaging is one deployment choice alongside an ordinary JAR and a [[Helidon Jlink Runtime Image]].

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
