2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Deployment and Platform Integration]]

# jpackage Self-Contained Java Applications

`jpackage` creates a self-contained Java application distribution that includes application code, dependencies, resources, and a suitable Java runtime. It entered preview in JDK 14 and became final in JDK 16. The resulting installation behaves like other software on the target operating system, removing the requirement that an end user install and configure a compatible shared JVM.

The tool can package nonmodular classpath applications, modular JAR or JMOD applications, and applications already linked into a custom runtime image. This replaces older assumptions behind applets and Java Web Start with an application-specific runtime that developers test as part of the product. Platform installers are built with native packaging facilities, so they are created for the operating system on which packaging occurs. See [[JavaFX jpackage Build Workflows]].

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
