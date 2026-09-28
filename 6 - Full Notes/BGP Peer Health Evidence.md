2026-09-27 22:03

Status: #baby

Tags: [[Evidence-Based Network Agent Troubleshooting]]

# BGP Peer Health Evidence

BGP peer health evidence combines aggregate counts with each neighbor’s state, uptime, and received-prefix count. Comparing `established_peers` with `total_peers` reveals whether the device has a degraded session even when the device itself is up, while the neighbor list identifies the exact peer that needs investigation.

An agent should report every state other than `Established` and retain the corresponding address and prefix evidence. A generic explanation of BGP is not evidence about current health; the conclusion must follow a current `bgp_summary` result or another authoritative observation.

# References

[[buildingaiagentsfornetworkoperations.pdf]]
