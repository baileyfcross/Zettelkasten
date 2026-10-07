2026-10-07 18:14

Status: #baby

Tags: [[SLES Networking Firewall and SELinux]]

# firewalld Zone Trust Model

Firewalld uses zones to associate incoming traffic with a chosen level of trust and a corresponding set of allowed services, ports, and rules. An interface or source is assigned to an ingress zone, and the zone policy determines which new connections are accepted while the stateful firewall continues to track established traffic.

The zone name is a policy label, not proof that a network is safe. SLES administrators should select a zone whose allowances match the connected environment and review changes made by service tools. Firewalld implements the policy through nftables underneath, but its managed abstraction should remain the normal configuration boundary.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
