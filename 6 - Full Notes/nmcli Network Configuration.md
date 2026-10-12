2026-10-07 18:14

Status: #baby

Tags: [[SLES Networking Firewall and SELinux]]

# nmcli Network Configuration

The `nmcli` command inspects and changes NetworkManager devices and connection profiles from the shell. It can list active connections, display detailed properties, create or modify profiles, activate a chosen profile, and report device state without requiring a graphical session.

Changes should distinguish saved configuration from current activation. Editing a profile does not necessarily replace the active settings until the connection is reapplied or reactivated, and disconnecting a remote interface can terminate the session used to repair it. [[SLES Network Connectivity Testing]] should verify the resulting address, route, name resolution, and reachability.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
