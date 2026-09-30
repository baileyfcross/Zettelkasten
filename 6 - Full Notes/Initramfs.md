2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Build and Configuration]]

# Initramfs

An initramfs is a compressed early user-space filesystem loaded into memory with the Linux kernel. It supplies an initial `init` program, tools, and modules needed before the permanent root filesystem can be reached.

This indirection is essential when the real root depends on storage, encryption, RAID, networking, or filesystem support that is not built directly into the kernel image. Early user space discovers and prepares the root device, mounts it, and transfers execution into the normal system.

# References

[[linuxkernelprogramming_secondedition.pdf]]
