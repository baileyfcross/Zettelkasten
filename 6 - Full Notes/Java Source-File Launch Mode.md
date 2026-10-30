2026-10-30 15:57

Status: #baby

Tags: [[Java Platform Runtime and Project Structure]]

# Java Source-File Launch Mode

Java's source-file launch mode lets the `java` launcher compile a source file in memory and immediately run its entry point. It removes the separate visible `javac` step for a small program while retaining ordinary Java compilation rules and the selected JDK's language level.

Newer preview forms can reduce ceremony further through implicitly declared classes and instance main methods. The mode is convenient for examples and scripts, but a multi-file application still benefits from explicit packages, build metadata, tests, and reproducible output directories.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
