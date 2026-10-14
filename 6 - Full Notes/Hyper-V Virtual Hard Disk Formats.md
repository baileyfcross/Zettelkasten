2026-10-14 00:45

Status: #baby

Tags: [[Windows Server Virtualization and Containers]]

# Hyper-V Virtual Hard Disk Formats

A Hyper-V virtual hard disk is a file that presents persistent block storage to a virtual machine. The older VHD format supports disks up to 2 TB and remains useful when compatibility with legacy systems matters. VHDX raises the maximum to 64 TB and adds larger block sizes, more efficient space use, and better protection against corruption caused by power failure.

Format selection is therefore a compatibility decision as well as a capacity decision. New [[Hyper-V Role|Hyper-V]] workloads generally benefit from VHDX resilience and scale, while a migration path may retain VHD until every target can consume the newer format. The disk file travels with the virtual machine's stored operating system, applications, and data, so its protection and placement are part of the workload's availability design.

# References

[[windowsserver2025administrationfundamentals_fourthedition.pdf]]
