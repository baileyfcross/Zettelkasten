2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Build and Configuration]]

# Linux Kernel Configuration

A Linux kernel configuration selects which features, drivers, debugging aids, and security controls a build contains. The resulting `.config` records Boolean, tristate, integer, and other choices; a tristate feature may be built into the image, built as a module, or omitted.

A useful configuration begins from a known target, such as an architecture default, a distribution configuration, or [[Localmodconfig]], and is then deliberately adjusted. Dependencies and visibility rules mean that one choice can enable, hide, or constrain others, so the saved configuration is part of the build's reproducible specification.

# References

[[linuxkernelprogramming_secondedition.pdf]]
