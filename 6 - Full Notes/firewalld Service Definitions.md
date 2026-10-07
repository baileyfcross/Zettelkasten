2026-10-07 18:14

Status: #baby

Tags: [[SLES Networking Firewall and SELinux]]

# firewalld Service Definitions

A firewalld service definition gives a named application service a reusable collection of ports, protocols, and related connection helpers. Zones can allow the service by name instead of repeating its low-level port set, making the rule express why traffic is open rather than only which numbers are accepted.

The definition must still match the application's actual listeners. A daemon moved to a nonstandard port or bound only to a particular address may not be reachable merely because the standard service is allowed. Custom definitions keep site-specific application requirements reviewable without replacing the zone model.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
