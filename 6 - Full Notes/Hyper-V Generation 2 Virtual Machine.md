2026-09-30 23:37

Status: #baby

Tags: [[Windows Server Virtualization and Containers]]

# Hyper-V Generation 2 Virtual Machine

A Hyper-V Generation 2 virtual machine uses UEFI-based virtual firmware and synthetic devices instead of emulating older BIOS-era hardware. It supports capabilities such as Secure Boot, booting from synthetic SCSI storage, and a cleaner modern device model. Current Windows Server guests are normally good candidates when legacy boot compatibility is unnecessary.

Generation is selected when the VM is created and is not a routine setting to toggle later. Installation media, guest operating system, Secure Boot template, and recovery tooling must therefore support the chosen model. Generation 1 remains relevant for older operating systems or software that expects legacy firmware and devices, but selecting it by habit forfeits newer security and boot features without improving a modern guest.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
