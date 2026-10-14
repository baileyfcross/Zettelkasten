2026-09-30 23:37

Status: #baby

Tags: [[Windows Server Virtualization and Containers]]

# Hyper-V Virtual Switch

A Hyper-V virtual switch connects virtual network adapters to one another and, depending on type, to the host or physical network. An external switch binds to a physical adapter, an internal switch connects VMs with the management operating system, and a private switch limits communication to VMs on the same host.

The switch is a policy and isolation point, not merely a graphical representation of a cable. VLANs, bandwidth controls, security extensions, and software-defined networking can shape its traffic. An external switch may temporarily interrupt connectivity when created and can share or dedicate the physical adapter to management traffic. Clustered hosts need consistent naming and reachability so a migrated VM attaches to an equivalent network on its destination.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
