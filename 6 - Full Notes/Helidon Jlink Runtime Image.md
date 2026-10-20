2026-10-19 22:48

Status: #baby

Tags: [[Helidon Platform Models and Project Tooling]]

# Helidon Jlink Runtime Image

Helidon-generated projects include a `Dockerfile.jlink` path that uses the JDK `jlink` tool to assemble a custom Java runtime image for the application. The image contains the selected runtime modules instead of an entire general-purpose JDK distribution.

The book presents this packaging route as a way to produce a smaller, more efficient container image. It remains distinct from [[Helidon GraalVM Native Image Packaging]], which compiles the application to a native executable rather than constructing a tailored Java runtime.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
