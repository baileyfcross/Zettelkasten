2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Deployment and Platform Integration]]

# JavaFX jpackage Build Workflows

The `jpackage` command separates generic options from settings for runtime images, application images, launchers, and native installers. It can be invoked directly after assembling application JARs and JavaFX modules, but the target platform may require its native installer tools, such as the WiX Toolset for Windows packages.

Build systems can make the same process repeatable. A Gradle project can use a jlink-oriented plugin to select modules, build a reduced runtime, and pass packaging metadata, icons, launch arguments, and installer choices into `jpackage`. The output can be a macOS disk image, Windows executable installer, or Linux package that users install conventionally. This workflow operationalizes the bundle described in [[jpackage Self-Contained Java Applications]].

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
