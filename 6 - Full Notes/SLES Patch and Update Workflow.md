2026-10-07 18:14

Status: #baby

Tags: [[SLES Software Lifecycle Management]]

# SLES Patch and Update Workflow

The SLES update workflow refreshes repository knowledge, reviews applicable patches or package changes, resolves the transaction, downloads verified content, and applies it while preserving evidence about the result. Security, recommended, and optional updates may carry different urgency, service impact, or reboot requirements.

A reliable workflow separates preview from execution and checks service health afterward. On a BTRFS system, Zypper integration with [[Snapper Snapshot and Rollback]] can create a recovery point around package changes, but a snapshot does not replace backups, compatibility testing, or a plan for clustered and stateful applications.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
