2026-10-07 18:14

Status: #baby

Tags: [[SLES Boot and Recovery Administration]]

# EFI System Partition

The EFI System Partition is a GPT-designated filesystem that stores boot executables and related files in locations UEFI firmware can read before the operating system starts. Multiple operating systems or boot components can place their own vendor paths on the same partition.

It is boot infrastructure rather than the Linux root filesystem. Damage, an incorrect firmware entry, or a missing loader can stop boot before the kernel or initramfs is involved. Recovery should therefore verify the partition, its filesystem, the expected loader path, and the matching UEFI entry as separate facts.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
