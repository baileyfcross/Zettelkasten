2026-10-30 15:57

Status: #baby

Tags: [[Java Platform Runtime and Project Structure]]

# Maven Java Project Layout

Maven gives a Java project a conventional structure and a declarative `pom.xml`. Production Java sources live under `src/main/java`, production resources under `src/main/resources`, tests under `src/test/java`, and test resources under `src/test/resources`; generated build output belongs under `target`.

This convention lets plugins find inputs without project-specific instructions. The POM identifies coordinates, dependencies, compiler settings, plugins, and modules, so compiling, testing, packaging, and documentation can be repeated outside an IDE. A Maven module is a build subproject and should not be confused with a named [[Java Platform Module System|Java module]].

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
