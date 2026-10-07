2026-10-07 18:14

Status: #baby

Tags: [[SLES Storage and Snapshot Administration]]

# LVM Logical Volume

An LVM logical volume is a virtual block device allocated from the extents of an [[LVM Volume Group]]. It can hold a filesystem, swap area, or another block-oriented consumer while presenting a stable device independent of the exact physical extents underneath.

Creating the logical volume allocates block capacity but does not automatically create or mount a filesystem. Those are separate layers with their own sizes and metadata. This distinction is essential during extension: increasing the logical volume alone does not guarantee that its filesystem can use the added space.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
