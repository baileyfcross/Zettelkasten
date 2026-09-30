2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Module Development]]

# Kernel Module Licensing

A kernel module declares its license through module metadata. Linux uses that declaration to distinguish licenses considered compatible with the kernel's GPLv2 terms, control access to GPL-only exported symbols, and report a proprietary or otherwise tainting module in the running kernel state.

The declaration is technically significant but is not a substitute for legal analysis. Linking, distribution, copied inline code, and the relationship between a module and the kernel can create obligations that a metadata string cannot settle by itself.

# References

[[linuxkernelprogramming_secondedition.pdf]]
