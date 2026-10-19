2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Deployment and Platform Integration]]

# JavaFX on Raspberry Pi

JavaFX runs on Raspberry Pi when the installed Java and JavaFX artifacts match its ARM architecture. The book configures a 64-bit Raspberry Pi 5 with Java 21 and the AArch64 JavaFX 23 SDK. That SDK contains ordinary JavaFX modules plus ARM-native libraries; an x86-64 Linux distribution is not interchangeable. The 64-bit build supports web and media modules, while Swing is not supported in the described environment.

Raspberry Pi OS can present JavaFX through its desktop window system, and Maven or Gradle can simplify module paths and execution. The platform's small size, GPIO access, display support, and capable GPU make it suitable for embedded interfaces. Local builds work, but desktop development and remote transfer are often faster, as described in [[Headless and Remote JavaFX on Raspberry Pi]].

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
