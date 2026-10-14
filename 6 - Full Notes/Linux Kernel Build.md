2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Build and Configuration]]

# Linux Kernel Build

A Linux kernel build transforms a saved [[Linux Kernel Configuration]] into an uncompressed `vmlinux`, an architecture-specific bootable image, and every selected loadable module. Parallel make jobs can shorten the build, but the source tree, toolchain, configuration, and generated files must all agree.

The uncompressed image is especially valuable for symbols and debugging even though the bootloader normally loads a compressed architecture image. Module installation, [[Initramfs]] generation, and bootloader configuration are separate deployment steps after compilation succeeds.

# References

[[linuxkernelprogramming_secondedition.pdf]]
