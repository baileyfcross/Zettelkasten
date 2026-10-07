2026-10-07 18:14

Status: #baby

Tags: [[SLES Storage and Snapshot Administration]]

# Snapper Snapshot and Rollback

Snapper manages BTRFS snapshots, including listing, creating, comparing, deleting, and using selected snapshots for rollback. Pre- and post-snapshot pairs can bracket an administrative change so file differences reveal what happened, and SLES integrates this model with Zypper transactions.

A rollback changes which filesystem state becomes the operational baseline; it is not simply a file-copy undo and may require a reboot to complete the system transition. Snapshots share the same storage and failure domain as the source filesystem, so they complement rather than replace backups and application-aware recovery.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
