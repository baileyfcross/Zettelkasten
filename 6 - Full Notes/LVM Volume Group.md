2026-10-07 18:14

Status: #baby

Tags: [[SLES Storage and Snapshot Administration]]

# LVM Volume Group

An LVM volume group pools extents from one or more [[LVM Physical Volume]] objects into an administrative capacity domain. Logical volumes allocate from that pool, so storage can be added, relocated, or assigned without requiring each filesystem to correspond directly to one fixed partition.

The abstraction makes capacity flexible but introduces dependencies that must be visible during repair. Removing a physical volume requires relocating allocated extents first, and a missing member can affect logical volumes spanning it. Capacity reports should distinguish total group space, allocated extents, and free extents.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
