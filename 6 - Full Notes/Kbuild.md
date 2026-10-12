2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Build and Configuration]]

# Kbuild

Kbuild is the Linux kernel's distributed build system. Makefiles throughout the source tree describe which objects are built into the kernel, which become modules, and how composite objects are assembled, often conditioning those decisions on symbols defined by [[Kconfig]].

Rules such as `obj-y` and `obj-m` connect a selected configuration to concrete compilation units. This lets each subsystem declare its local build structure while the top-level build coordinates architecture settings, generated headers, dependencies, and final images.

# References

[[linuxkernelprogramming_secondedition.pdf]]
