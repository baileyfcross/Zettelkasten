2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Deployment and Platform Integration]]

# GluonFX Mobile Compilation

GluonFX plugins hide much of the cross-compilation and packaging work required to turn a JavaFX project into iOS or Android applications. They coordinate the target operating system and architecture, native toolchains, GraalVM, signing, and the bundle structures expected by mobile app stores. Developers can use Maven or Gradle while continuing to write against Java and JavaFX APIs.

The recommended flow is to write, compile, and test on a desktop JVM before producing a native mobile image. iOS builds require Apple tooling or an appropriate remote workflow, while Android builds use Linux tooling with the Android SDK and NDK. Ahead-of-time compilation is especially important on iOS because dynamically generated optimized code is not allowed. Configuration details are handled through [[JavaFX Native Image Resource Configuration]].

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
