2026-09-30 23:37

Status: #baby

Tags: [[Windows Remote Desktop Services]]

# Remote Desktop Collection

A Remote Desktop collection groups Session Hosts and defines the desktops, RemoteApp programs, user groups, profile behavior, and session settings offered as one service. The Connection Broker uses the collection boundary when placing and reconnecting sessions, letting a deployment host different application sets or user populations on separate pools.

All hosts in one collection should present compatible applications and configuration so a user receives the same environment regardless of placement. Collection settings can limit idle or disconnected sessions and specify profile disks or FSLogix-backed profiles. Adding a server increases capacity only when applications, policy, certificates, and networking are consistent. Collections should therefore align with workload compatibility and maintenance boundaries rather than being created merely to mirror organizational departments.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
