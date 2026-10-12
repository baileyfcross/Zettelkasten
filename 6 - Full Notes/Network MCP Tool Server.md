2026-09-27 22:03

Status: #baby

Tags: [[Network MCP Tool Architecture]]

# Network MCP Tool Server

A network MCP tool server publishes approved network capabilities through Model Context Protocol so multiple clients can discover and invoke the same interface. The server maps public tools such as device status, interface status, BGP summary, bounded ping, topology, and read-only show commands to internal safety wrappers.

The server is an exposure layer, not the place to hide network policy. Validation and business rules remain in [[Safe Network Tool Wrapper]] functions, while backend code obtains the data. This separation keeps transport changes from rewriting the operational controls.

# References

[[buildingaiagentsfornetworkoperations.pdf]]
