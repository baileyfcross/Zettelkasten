2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Deployment and Platform Integration]]

# GraalVM Native Image for JavaFX

GraalVM Native Image moves Java compilation to build time. Instead of shipping bytecode that a bundled JVM later interprets and compiles just in time, the build performs ahead-of-time compilation and links a platform-native executable. A JavaFX project should first be built and run normally before its native compile and link stages are attempted.

Native-image builds depend on target-specific toolchains: Xcode on macOS, development tools on Linux, and supported Visual Studio C++ components on Windows. Maven and Gradle plugins coordinate the process, but closed-world analysis must know about reflective access, resources, JNI, and dynamically reached classes. Those concerns are especially visible in the mobile configuration described by [[JavaFX Native Image Resource Configuration]].

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
