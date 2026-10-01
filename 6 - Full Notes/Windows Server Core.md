2026-09-30 23:37

Status: #baby

Tags: [[Windows Server Deployment and Administration]]

# Windows Server Core

Windows Server Core installs the server operating system without the full Desktop Experience shell. Its smaller component set reduces disk use, patching surface, restart pressure, and opportunities for attack. It still supports many major roles, including domain controller, DNS, DHCP, file, web, and Hyper-V workloads, but assumes that routine administration will occur remotely or through command-line tools.

Core is managed with SConfig for initial settings, PowerShell, Server Manager, remote MMC consoles, and [[Windows Admin Center]]. The absence of a local desktop should be treated as an architectural choice, not an incomplete installation. Role compatibility and the administrators' remote-management readiness should be confirmed before deployment because switching freely between Core and Desktop Experience is not the normal operating model.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
