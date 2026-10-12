2026-10-07 18:14

Status: #baby

Tags: [[SLES Boot and Recovery Administration]]

# SLES Rescue and Emergency Targets

SLES rescue and emergency targets provide reduced systemd environments for repair. Rescue mode brings up a minimal set of services and local filesystems for single-user administration, while emergency mode provides an even smaller shell-oriented state when ordinary mounting or dependencies cannot succeed.

The chosen target should match the failed layer. Entering emergency mode can expose a root filesystem that is read-only or incompletely mounted, so repairs may require deliberate remounting and later verification. These targets are recovery tools, not substitutes for fixing the dependency or configuration that prevented normal boot.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
