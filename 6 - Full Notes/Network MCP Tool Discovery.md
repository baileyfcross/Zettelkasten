2026-09-27 22:03

Status: #baby

Tags: [[Network MCP Tool Architecture]]

# Network MCP Tool Discovery

Network MCP tool discovery lets a client establish a session and retrieve the public tools registered by a network tool server. The discovered names and descriptions tell the client that capabilities such as device status, BGP summary, interface lookup, ping, topology, and constrained show commands are available.

Discovery confirms only the published interface. The client should still verify expected tools and contracts, and the server must authenticate and authorize callers before real infrastructure is exposed. Clear, non-overlapping descriptions improve selection without granting permission by themselves.

# References

[[buildingaiagentsfornetworkoperations.pdf]]
