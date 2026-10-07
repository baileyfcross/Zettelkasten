2026-10-07 18:14

Status: #baby

Tags: [[SLES Boot and Recovery Administration]]

# UEFI Firmware Boot Flow

UEFI firmware initializes the platform, reads boot entries stored in nonvolatile memory, and launches a selected executable from an [[EFI System Partition]]. Each entry can name a device and file path, and firmware boot order determines which candidate is tried by default.

This separates firmware selection from later GRUB and kernel configuration. The §efibootmgr§ utility can inspect and manage entries from Linux, but an incorrect change can make an otherwise healthy installation unreachable. SLES treats UEFI as the recommended modern boot environment, while legacy BIOS support is deprecated for new installations.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
