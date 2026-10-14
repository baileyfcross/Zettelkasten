2026-10-07 18:14

Status: #baby

Tags: [[SLES Storage and Snapshot Administration]]

# Persistent Filesystem Mounts with fstab

The `/etc/fstab` file declares filesystems that should be mounted with specified targets, types, options, and boot-time handling. Stable identifiers such as filesystem UUIDs avoid tying the declaration to a device name that may change when hardware discovery order changes.

An invalid entry can delay boot or force recovery, so a new declaration should be syntax-checked and tested with the mount tools before reboot. Network and optional storage may need explicit dependency or failure behavior so an unavailable resource does not prevent the rest of the system from reaching an appropriate target.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
