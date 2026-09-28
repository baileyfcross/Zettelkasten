2026-09-27 22:03

Status: #baby

Tags: [[Evidence-Based Network Agent Troubleshooting]]

# Network Reachability Causality Boundary

The network reachability causality boundary distinguishes proof that a target did not respond from proof of why it did not respond. A bounded ping result can confirm packet loss or an unreachable status, but it cannot by itself identify BGP, a static route, filtering, an interface, or the host as the root cause.

An agent may correlate failed reachability with an idle peer, zero received prefixes, or a down server-facing interface and present those as investigation directions. It should not promote that correlation to certainty unless a tool directly verifies the missing path and its cause.

# References

[[buildingaiagentsfornetworkoperations.pdf]]
