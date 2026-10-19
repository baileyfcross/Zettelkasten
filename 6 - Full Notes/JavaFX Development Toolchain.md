2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Application Architecture]]

# JavaFX Development Toolchain

A JavaFX development environment combines a modern OpenJDK, a matching JavaFX SDK or build dependency, an IDE or editor, and a build tool. The book uses OpenJDK 23 and JavaFX 23, with platform-specific JavaFX libraries supplied by Gluon. On Windows the JDK location is commonly exposed through `JAVA_HOME` and its `bin` directory is placed on `Path`; Linux distributions can install a matching JDK through their package managers.

JavaFX applications can be developed in IntelliJ IDEA, NetBeans, Eclipse, or Visual Studio Code. Maven or Gradle can resolve modules and run project tasks, while Scene Builder edits FXML visually. Keeping toolkit versions and native artifacts aligned with the target platform prepares the same project for later workflows such as [[JavaFX jpackage Build Workflows]], [[GluonFX Mobile Compilation]], and [[JavaFX on Raspberry Pi]].

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
