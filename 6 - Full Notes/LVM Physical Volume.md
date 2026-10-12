2026-10-07 18:14

Status: #baby

Tags: [[SLES Storage and Snapshot Administration]]

# LVM Physical Volume

An LVM physical volume is a block device or partition initialized for allocation by the Logical Volume Manager. LVM records metadata describing the device and divides its usable capacity into extents that a volume group can pool.

Initialization does not itself create a mountable filesystem. The physical volume becomes useful after joining an [[LVM Volume Group]], and its existing contents must be treated as expendable before creation. Inventory commands should confirm the selected device and reveal whether it already belongs to an LVM configuration.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
