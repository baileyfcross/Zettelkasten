2026-10-07 18:14

Status: #baby

Tags: [[SLES Software Lifecycle Management]]

# RPM Package Metadata and File Ownership

The RPM database records installed package names, versions, architecture, dependencies, scripts, signatures, and the files each package owns. Queries can identify the package that supplied a path, list a package's contents, or compare installed files with recorded size, digest, mode, owner, and other attributes.

This makes RPM evidence useful below Zypper's repository and dependency layer. An unexpected file may be a locally created artifact rather than package damage, and a modified configuration file may be intentional. Verification reports differences; the administrator must interpret them in the system's operational context.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
