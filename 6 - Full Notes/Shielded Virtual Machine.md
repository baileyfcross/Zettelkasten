2026-09-30 23:37

Status: #baby

Tags: [[Windows Server Virtualization and Containers]]

# Shielded Virtual Machine

A shielded virtual machine protects a Generation 2 Hyper-V guest from an administrator who controls the virtualization fabric but should not inspect or alter the tenant workload. BitLocker encrypts the virtual disks, a virtual TPM supports protected key release, and restricted management paths prevent ordinary console or offline disk access.

Host Guardian Service attests that a Hyper-V host belongs to the trusted fabric and releases the material required to start an authorized shielded VM. Shielding therefore shifts trust from each fabric operator to the guarded-fabric design, its signing and encryption certificates, and its recovery process. Losing guardian configuration or keys can make protected workloads unavailable, so backups and break-glass procedures are as important as preventing unauthorized inspection.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
