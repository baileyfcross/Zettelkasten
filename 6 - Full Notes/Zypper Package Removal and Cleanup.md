2026-10-07 18:14

Status: #baby

Tags: [[SLES Software Lifecycle Management]]

# Zypper Package Removal and Cleanup

Zypper package removal asks the dependency solver to remove selected packages and resolve the effect on dependent or no-longer-needed software. Removing a package does not necessarily remove every configuration file, generated datum, user account, cache, or external volume associated with the application.

Cleanup should distinguish package-managed files from administrator or application state. Reviewing the transaction protects shared dependencies, while [[RPM Package Metadata and File Ownership]] can identify which installed package owns a path. Repository removal is a different action and does not uninstall content previously installed from that source.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
