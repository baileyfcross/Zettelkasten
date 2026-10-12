2026-10-07 18:14

Status: #baby

Tags: [[SLES Storage and Snapshot Administration]]

# SLES Filesystem Creation and Mounting

Filesystem creation writes the structures used to name, allocate, and track files within a chosen block device or logical volume. Mounting then attaches that filesystem's root to a directory in the live Linux namespace; it does not copy its contents into the directory.

Formatting and mounting solve different problems and are both target-sensitive. Creating a filesystem can destroy the previous on-disk interpretation, while mounting on a nonempty directory temporarily hides the directory's existing contents. Persistent activation belongs in [[Persistent Filesystem Mounts with fstab]] after the one-time mount has been tested.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
