2026-10-07 18:14

Status: #baby

Tags: [[SLES Networking Firewall and SELinux]]

# NetworkManager Connection Profiles

A NetworkManager connection profile is a stored set of network settings that can be applied to a compatible interface. It can describe addresses, routes, DNS, gateway behavior, activation policy, and device-specific properties independently from the transient link object currently carrying traffic.

This separation lets one interface use different configurations in different environments and lets one profile be inspected before activation. On SLES, graphical, text, and command-line front ends operate on the same NetworkManager model, so diagnosis should compare the active connection, saved profile, and physical device rather than treating them as one object.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
