2026-09-30 23:37

Status: #baby

Tags: [[Windows Server Networking and Remote Access]]

# Windows Routing Table

The Windows routing table determines which interface and next hop carry a packet toward its destination. Directly connected networks appear from interface address and prefix configuration, a default route handles destinations without a more specific match, and static routes can add paths to known remote networks. The most specific applicable route is preferred, with metrics helping choose among comparable paths.

Multi-homed servers require special care because multiple default gateways can create asymmetric or unpredictable traffic. A server usually needs one default path and explicit routes for networks reached through another interface. The `route print` and PowerShell networking commands expose the effective table, which should be checked before blaming DNS or a firewall: a packet cannot reach the intended security boundary if the host first selects the wrong next hop.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
