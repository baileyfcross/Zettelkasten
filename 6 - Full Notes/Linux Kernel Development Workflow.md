2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Build and Configuration]]

# Linux Kernel Development Workflow

Linux kernel changes normally move through subsystem maintainers rather than directly into the mainline tree. Contributors prepare focused patches, test them, follow the subsystem's submission conventions, and respond to public review before a maintainer carries accepted work upward.

The merge window integrates subsystem trees after a final release, and successive release candidates emphasize stabilization. Stable and long-term branches then backport suitable fixes without treating every new mainline feature as appropriate for an already released kernel.

# References

[[linuxkernelprogramming_secondedition.pdf]]
