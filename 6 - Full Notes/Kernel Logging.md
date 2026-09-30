2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Module Development]]

# Kernel Logging

Linux kernel code emits diagnostic records with `printk` and convenience macros such as `pr_info` or `pr_err`. The records enter the kernel's ring buffer, from which tools such as `dmesg` and systemd's journal can retrieve them.

Logging is available where ordinary user-space output libraries are not, but excessive messages can distort timing and flood limited buffers. Rate-limited macros, consistent prefixes, portable format specifiers, and carefully chosen [[Kernel Log Levels]] make messages useful without turning observation into a new failure mode.

# References

[[linuxkernelprogramming_secondedition.pdf]]
