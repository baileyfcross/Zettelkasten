2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Build and Configuration]]

# Kconfig

Kconfig is the declarative language and file hierarchy that defines Linux kernel configuration symbols and presents them through configuration interfaces such as `menuconfig`. Entries can specify a type, prompt, default, valid range, help text, dependencies, and reverse dependencies.

Kconfig determines which choices are meaningful and visible for a target, while [[Kbuild]] determines what those choices cause the build to compile. A symbol selected as built-in or modular becomes available to C code and build rules through generated configuration data.

# References

[[linuxkernelprogramming_secondedition.pdf]]
