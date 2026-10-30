2026-10-30 15:57

Status: #baby

Tags: [[Java Diagnostics Testing and Documentation]]

# Maven Java Test Source Layout

In a Maven Java project, production code belongs under `src/main/java` and test code under `src/test/java`, with corresponding resource directories. Tests can mirror production package names while remaining in a separate source set and classpath.

Maven's test phase compiles the main code first, adds test dependencies, compiles tests, and invokes the configured test provider. This separation keeps testing libraries and fixtures out of the production artifact while giving tests access to the public and package-visible behavior their package arrangement permits.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
