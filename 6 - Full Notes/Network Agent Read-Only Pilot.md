2026-09-27 22:03

Status: #baby

Tags: [[Production Network Agent Operations]]

# Network Agent Read-Only Pilot

A network agent read-only pilot lets approved users query approved real systems without granting the agent permission to change network state. It can enrich alerts, inspect interfaces and BGP, check bounded reachability, and prepare handoffs while the team evaluates evidence quality, access control, failure behavior, and operational usefulness.

Read-only is a reduced blast radius, not an absence of risk. Queries can expose sensitive state, overload devices, or support a misleading summary. The pilot therefore still requires allowlists, bounded tools, validation, audit events, monitoring, ownership, acceptance criteria, and a tested disable path.

# References

[[buildingaiagentsfornetworkoperations.pdf]]
