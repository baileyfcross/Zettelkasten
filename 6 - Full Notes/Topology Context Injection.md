2026-09-27 18:30

Status: #baby

Tags: [[Network Copilot Design]]

# Topology Context Injection

Topology context injection supplies a copilot with explicit device-to-device connections, interfaces, VLAN roles, subnets, and dependencies. It lets the assistant answer questions about where a port leads or what could be affected by a change instead of reasoning from isolated device facts.

Only the neighborhood needed for the question should enter the prompt, especially in a large network. Direction, interface pairing, and topology version must be preserved. An old or incomplete link map can make a fluent answer more dangerous, which is why [[Network Knowledge Refresh]] is part of the design.

# References

[[ainetworkingcookbook.pdf]]
