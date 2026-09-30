2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Module Development]]

# Kernel Module Autoloading

Kernel module autoloading connects a request for a capability or a discovered device to user-space module tools that locate and insert a matching module. Module aliases and generated dependency metadata allow the loader to choose the object and bring in prerequisites.

Boot-time configuration can also name modules that should load regardless of immediate hardware discovery. Autoloading is convenient but part of the system's attack surface, so deployments may restrict loading, require signatures, or disable further module insertion after initialization.

# References

[[linuxkernelprogramming_secondedition.pdf]]
