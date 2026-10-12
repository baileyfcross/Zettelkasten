2026-10-07 18:14

Status: #baby

Tags: [[SLES Storage and Snapshot Administration]]

# GPT and MBR Partition Tables on SLES

A disk partition table records the boundaries and types of regions made available for filesystems, swap, LVM, or boot data. MBR uses an older layout with size and primary-partition constraints, while GPT supports modern large disks, more entries, redundant metadata, and the partition types expected by UEFI systems.

Changing the table is a lower-layer storage operation that can make every higher-layer object inaccessible if boundaries are wrong. SLES administrators should confirm the exact device and existing layout, preserve needed boot partitions, and distinguish a partition from the filesystem or LVM object it may contain.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
