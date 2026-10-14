2026-10-07 18:14

Status: #baby

Tags: [[SLES Storage and Snapshot Administration]]

# Online LVM Volume Extension

Online LVM extension increases an [[LVM Logical Volume]] from free extents in its volume group and then expands a supported filesystem so the mounted namespace can use the new blocks. The block layer and filesystem layer are distinct even when one command can coordinate both steps.

The administrator should confirm free capacity, the target logical volume, and filesystem growth support before changing either layer. Extension is normally easier than reduction because shrinking requires moving live filesystem content and is not supported by every filesystem; extra allocated blocks should not be mistaken for extra usable file space until growth completes.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
