2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Module Development]]

# Linux Kernel ABI Stability

The upstream Linux kernel does not promise a stable internal binary interface for out-of-tree modules. Data structures, exported symbols, configuration details, and compiler-generated layouts may change across kernel builds even when the module source still looks compatible.

A module should therefore be built for the exact target kernel and its configuration, or maintained through a compatibility layer that is actively tested. A version string alone cannot guarantee loadability because symbol versioning and build-time choices also participate in the interface.

# References

[[linuxkernelprogramming_secondedition.pdf]]
