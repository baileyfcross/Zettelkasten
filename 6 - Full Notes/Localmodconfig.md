2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Build and Configuration]]

# Localmodconfig

`localmodconfig` derives a smaller Linux kernel configuration from the modules currently loaded on the running system. It can greatly reduce build time and eliminate drivers that appear irrelevant to that machine.

Its evidence is necessarily incomplete: hardware not attached during configuration, rarely used filesystems, recovery devices, or modules needed only during boot may be missed. The generated configuration is therefore a starting point to review, not proof that every future workload will boot and operate correctly.

# References

[[linuxkernelprogramming_secondedition.pdf]]
