2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Build and Configuration]]

# Linux Kernel Boot Process

Linux boot begins with platform firmware transferring control to a bootloader, which loads the selected kernel image and usually an [[Initramfs]] into memory together with kernel command-line parameters. The kernel decompresses, initializes architecture and core subsystems, and starts early user space.

The initramfs prepares the permanent root filesystem when necessary. After switching to that root, the system starts its normal initialization process and services. A boot failure can therefore originate in firmware selection, bootloader configuration, kernel configuration, early-user-space contents, command-line parameters, or root-device discovery.

# References

[[linuxkernelprogramming_secondedition.pdf]]
