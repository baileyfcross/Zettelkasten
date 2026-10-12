2026-09-30 23:37

Status: #baby

Tags: [[Windows Remote Desktop Services]]

# Remote Desktop Session Host

A Remote Desktop Session Host runs multiple interactive Windows user sessions on one server and supplies the desktops or applications published through an RDS collection. Users share the host's operating system and hardware while receiving separate session state. Multiple Session Hosts can form a farm so capacity and maintenance do not depend on one server.

Applications must be installed and tested for multi-user behavior, and sizing must consider concurrent sessions rather than only the number of accounts. Group Policy, profiles, antivirus exclusions, updates, and application compatibility all affect logon and session performance. The Session Host should not also carry unrelated infrastructure roles. [[Remote Desktop Connection Broker]] directs users among hosts and reconnects them to existing sessions, while drain mode prepares one host for controlled maintenance.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
