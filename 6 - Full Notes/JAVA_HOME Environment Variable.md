2026-10-30 15:57

Status: #baby

Tags: [[Java Platform Runtime and Project Structure]]

# JAVA_HOME Environment Variable

`JAVA_HOME` identifies the root directory of a selected JDK installation. Build tools and scripts use it to locate the Java toolchain without embedding a machine-specific installation path, while the operating system's `PATH` commonly includes the JDK's `bin` directory so commands such as `java` and `javac` can be invoked directly.

The variable must point to the JDK directory rather than to the executable itself. When several JDKs are installed, changing `JAVA_HOME` and the related path selection determines which compiler and runtime a command-line build will use.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
