2026-10-07 18:14

Status: #baby

Tags: [[SLES Storage and Snapshot Administration]]

# BTRFS Copy-on-Write Subvolume

BTRFS uses copy-on-write so changed blocks are written to new locations and metadata is updated to reference the new version instead of overwriting every old block in place. A subvolume is an independently managed filesystem tree within the larger BTRFS filesystem and can serve as a boundary for mounting and snapshots.

Subvolumes share the same underlying storage pool, so they are not isolated partitions with fixed capacity. Copy-on-write enables efficient snapshots, but a snapshot is not an independent backup when it resides on the same device. SLES uses BTRFS for the default operating-system filesystem and relies on [[Snapper Snapshot and Rollback]] for managed snapshot operations.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
