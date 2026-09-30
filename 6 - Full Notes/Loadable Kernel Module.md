2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Module Development]]

# Loadable Kernel Module

A loadable kernel module is compiled kernel code that can be inserted into and removed from a running Linux kernel. It extends the monolithic kernel without requiring every optional driver or feature to remain permanently linked into the boot image.

Once loaded, a module executes with kernel privilege and shares the kernel address space, so an invalid pointer or synchronization error can affect the whole system. The framework provides lifecycle hooks, metadata, parameters, exported symbols, dependency handling, and build integration, but it does not create process-like isolation.

# References

[[linuxkernelprogramming_secondedition.pdf]]
