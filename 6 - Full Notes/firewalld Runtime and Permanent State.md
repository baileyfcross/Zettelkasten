2026-10-07 18:14

Status: #baby

Tags: [[SLES Networking Firewall and SELinux]]

# firewalld Runtime and Permanent State

Firewalld maintains a runtime configuration used by the active firewall and a permanent configuration loaded for future starts or reloads. A runtime-only change is useful for testing because it can disappear on reload, while a permanent-only change does not immediately alter the live packet path.

Operational errors arise when an administrator verifies one state but records the other. A safe workflow makes the intended change, tests it from the required source, and then explicitly preserves or removes it. Reloading remotely should account for the possibility that the new permanent policy may close the current management path.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
