2026-10-07 18:14

Status: #baby

Tags: [[SLES Software Lifecycle Management]]

# Zypper Repository Management

Zypper repository management controls the named software sources from which metadata and packages are resolved. A repository definition includes a location and state such as enabled, disabled, or refresh behavior, while metadata refresh updates the local view of what that source currently offers.

Repository identity, reachability, entitlement, and signature trust are separate checks. Duplicated or obsolete sources can create ambiguity and solver conflicts, but removing a repository does not uninstall packages already obtained from it. Administrators should record why each source exists before changing the set.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
