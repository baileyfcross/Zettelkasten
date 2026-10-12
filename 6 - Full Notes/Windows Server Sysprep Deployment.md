2026-09-30 23:37

Status: #baby

Tags: [[Windows Server Deployment and Administration]]

# Windows Server Sysprep Deployment

Sysprep prepares a Windows Server installation to become a reusable deployment image by removing machine-specific identity and returning the next boot to the out-of-box experience. A common template workflow is to install the operating system, apply updates and shared customization, avoid binding the image to workload-specific roles, and run `sysprep.exe /generalize /oobe /shutdown`.

The generalized disk or VHDX is copied only while the template remains shut down. Each clone then boots through initialization and receives its own name, identity, address, and role configuration. This separates a stable operating-system baseline from the later configuration of individual servers. Rebooting the generalized template before preserving the image can consume the prepared state and undermine repeatability.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
