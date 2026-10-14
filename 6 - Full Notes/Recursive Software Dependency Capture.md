2026-09-28 21:33

Status: #baby

Tags: [[Computational Environment Portability]]

# Recursive Software Dependency Capture

Recursive software dependency capture identifies not only the program explicitly invoked but also the libraries, interpreters, packages, and lower-level components on which it depends. Versions and source-control identities are preferable to an unqualified package name because behavior can change between releases.

This record supports reconstructing an environment without assuming that the researcher knew every indirect dependency. It can be combined with [[Runtime File Access Capture]] to observe what a run actually touches or with a [[Lightweight Execution Environment Package]] to preserve the discovered files themselves.

# References

[[implementingreproducableresearch.pdf]]
