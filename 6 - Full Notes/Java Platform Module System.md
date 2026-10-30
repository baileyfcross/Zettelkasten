2026-10-30 15:57

Status: #baby

Tags: [[Java Platform Runtime and Project Structure]]

# Java Platform Module System

The Java Platform Module System groups packages and resources into uniquely named reusable units. Introduced with Java 9, it modularized both the JDK and applications, allowing dependencies and exported APIs to be declared instead of inferred only from a flat classpath.

A module creates two related boundaries: readability determines which other modules it depends on, and exports determine which of its packages are accessible to dependents. This stronger configuration can reveal missing dependencies or split packages earlier and allows a runtime image to include only the JDK modules an application requires.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
