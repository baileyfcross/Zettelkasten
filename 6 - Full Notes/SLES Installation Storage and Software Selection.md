2026-10-07 18:14

Status: #baby

Tags: [[SLES Installation and Shell Operations]]

# SLES Installation Storage and Software Selection

SLES installation storage selection determines which devices are used, how the system is partitioned, and where the operating system and its data will reside. Software selection determines the initial package patterns and capabilities installed on that layout. Both are proposals that should be reviewed against the server's intended role rather than accepted solely because they boot.

The choices have long consequences: a BTRFS root can support [[Snapper Snapshot and Rollback]], while additional workloads may require separate capacity or packages. Later changes remain possible, but changing an installed storage design is usually more disruptive than revising the installer proposal.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
