2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Build and Configuration]]

# Linux Kernel Cross-Compilation

Linux kernel cross-compilation builds for a target architecture using a toolchain that runs on a different host architecture. The build identifies the target through `ARCH` and selects the compiler family with `CROSS_COMPILE`.

Configuration must describe the target platform rather than the host, and installation artifacts must be placed where the target system can use them. A kernel, its modules, device-tree data when required, and early userspace must be built as one compatible deployment set.

# References

[[linuxkernelprogramming_secondedition.pdf]]
