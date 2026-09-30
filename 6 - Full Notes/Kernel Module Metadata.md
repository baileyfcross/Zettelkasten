2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Module Development]]

# Kernel Module Metadata

Linux kernel module macros embed descriptive and operational metadata in the module object. Common fields identify the author, description, license, version, aliases, and parameters, allowing module tools and the kernel to inspect the code without executing its main behavior.

Metadata is not merely documentation. The declared license can affect access to GPL-only exported symbols and whether the kernel marks itself tainted, while aliases help user space associate hardware or another request with the module that should be loaded.

# References

[[linuxkernelprogramming_secondedition.pdf]]
