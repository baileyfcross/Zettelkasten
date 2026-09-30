2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Build and Configuration]]

# GRUB Kernel Selection

GRUB presents installed kernels as boot entries and passes the chosen image, initramfs, and command line to the machine. Installing a custom kernel therefore requires a matching boot entry and a way to retain or select a known-working fallback.

The configured default can name a menu entry, while the interactive prompt permits temporary inspection or changes. Keeping an older bootable kernel is a recovery measure when a new [[Linux Kernel Build]] cannot locate its root filesystem or complete initialization.

# References

[[linuxkernelprogramming_secondedition.pdf]]
