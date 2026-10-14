2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Build and Configuration]]

# Linux Kernel Source Tree

The Linux kernel source tree separates architecture-specific code, device drivers, filesystems, memory management, core kernel services, headers, documentation, build scripts, and development tools into recognizable top-level regions.

This layout is also a map of responsibility. A change belongs near the subsystem it affects, while shared interfaces live in common headers or core directories. The tree's `MAINTAINERS` file connects paths and subsystems to the people and review channels responsible for them.

# References

[[linuxkernelprogramming_secondedition.pdf]]
