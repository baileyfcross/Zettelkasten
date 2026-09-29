2026-09-28 21:33

Status: #baby

Tags: [[Computational Environment Portability]]

# Lightweight Execution Environment Package

A lightweight execution environment package contains the code, data, dependencies, and selected system files actually needed by a computation without bundling an entire operating system. It can be built by monitoring execution and copying accessed resources into a mirrored directory tree.

Compared with a [[Virtual Machine]], this package can be much smaller and leaves scripts and data directly editable. Its portability is narrower because it still relies on a compatible architecture and operating-system kernel. [[Filesystem Redirection for Portable Execution]] can replay the computation against the packaged tree without installing its software globally.

# References

[[implementingreproducableresearch.pdf]]
