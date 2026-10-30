2026-10-30 16:54

Status: #baby

Tags: [[Java Source Launch and Documentation]]

# Java Multi-File Source Launcher

The Java multi-file source launcher runs a source program whose referenced classes reside in separate Java files without an explicit prior compilation step. Starting the main source causes the launcher to discover and compile required source dependencies before invoking its entry method.

This removes the earlier pressure to place several public classes in one file merely to retain source-launch convenience. Small programs can acquire normal file structure gradually and can include external JARs through the classpath before they need a full Maven or Gradle build.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
