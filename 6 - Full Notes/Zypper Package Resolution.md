2026-10-07 18:14

Status: #baby

Tags: [[SLES Software Lifecycle Management]]

# Zypper Package Resolution

Zypper resolves a requested package operation against enabled repositories, installed packages, dependencies, conflicts, architecture, and available versions before applying changes. The proposed transaction may therefore add, update, replace, or remove more packages than the name typed on the command line.

Reviewing the solver proposal is part of the operation. A missing package may indicate a disabled module or stale repository metadata, while a conflict can reveal incompatible requirements rather than a download failure. The local RPM database records the result after Zypper has made the repository-level decision.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
