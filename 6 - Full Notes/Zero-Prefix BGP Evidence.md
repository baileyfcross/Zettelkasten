2026-09-27 22:03

Status: #baby

Tags: [[Evidence-Based Network Agent Troubleshooting]]

# Zero-Prefix BGP Evidence

Zero-prefix BGP evidence indicates that a peer is contributing no routes in the observed summary. When the same neighbor is idle or otherwise not established, the value supports investigating whether missing reachability depends on routes expected through that session.

Zero prefixes do not independently prove the cause of a particular outage. The design may intentionally receive no routes, the relevant prefix may use another source, or the exact routing table may not have been checked. A troubleshooting response should connect the value to a hypothesis while preserving those unknowns.

# References

[[buildingaiagentsfornetworkoperations.pdf]]
