2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Build and Configuration]], [[SLES Boot and Recovery Administration]]

# Initramfs

An initramfs is a compressed early user-space filesystem loaded into memory with the Linux kernel. It supplies an initial `init` program, tools, and modules needed before the permanent root filesystem can be reached.

This indirection is essential when the real root depends on storage, encryption, RAID, networking, or filesystem support that is not built directly into the kernel image. Early user space discovers and prepares the root device, mounts it, and transfers execution into the normal system.

In the SLES boot sequence, an initramfs problem appears after GRUB has loaded the selected artifacts but before systemd can operate from the permanent root. Recovery should confirm that the image matches the kernel and contains the drivers and configuration needed to locate that root.

# References

[[linuxkernelprogramming_secondedition.pdf]]
[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
