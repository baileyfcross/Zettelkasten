2026-09-27 22:03

Status: #baby

Tags: [[Production Network Agent Operations]]

# Network Agent Device Allowlist

A network agent device allowlist defines the devices, groups, or environments that a tool may target. The wrapper checks a requested identifier against that scope before contacting a backend and returns a structured rejection for unknown or excluded devices.

An allowlist limits blast radius and prevents a plausible model-generated hostname from becoming an execution target. It must be tied to current inventory and authorization rather than copied permanently into a prompt. Production review should identify who owns the list, how it changes, and which users may access each portion.

# References

[[buildingaiagentsfornetworkoperations.pdf]]
