2026-10-07 18:14

Status: #baby

Tags: [[SLES Administration Interfaces and Automation]]

# Cockpit Storage and Network Administration

Cockpit can expose storage devices, filesystems, mounts, and network interfaces through browser workflows that invoke the host's normal management services. The interface makes relationships easier to inspect, but the resulting partition, mount, or NetworkManager change has the same system-wide effect as its command-line equivalent.

Remote changes require particular caution because reconfiguring the active interface, route, mount, or storage device can remove the path used to manage the host. Administrators should verify the target object and preserve an alternate recovery path before applying a disruptive operation.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
