2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Build and Testing]]

# ClusLib Header Naming Convention

ClusLib limits file and directory names to lowercase ASCII letters and numbers, uses .hpp for C++ headers, and uses .cpp for source files. Subject directories contain the paired declarations and definitions for their components.

A predictable convention reduces platform-sensitive naming problems and lets generated umbrella headers enumerate public headers mechanically. Consistency also makes build specifications and include paths easier to audit.

# References

[[dataclusteringincplusplus.pdf]]

