2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Deployment and Platform Integration]]

# JavaFX Raspberry Pi Native Images

A JavaFX application can be compiled into a native AArch64 image for Raspberry Pi. Because native-image generation consumes substantial CPU and memory, the book recommends cross-compiling on an x86-64 Linux workstation rather than performing the build on the device. The resulting binary targets the Pi's architecture and can run without a separately installed application JVM.

Cross-compilation makes deployment a build concern: JavaFX modules, third-party dependencies, native libraries, resources, and dynamic reachability metadata must all be included for the target. Once produced, the artifact can be transferred and launched with the remote techniques in [[Headless and Remote JavaFX on Raspberry Pi]]. The process applies [[GraalVM Native Image for JavaFX]] to an embedded rather than desktop target.

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
