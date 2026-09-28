2026-09-27 12:11

Status: #baby

Tags: [[DevOps Agent Memory and MCP]] [[Network MCP Tool Architecture]]

# MCP Tool Contract Testing

MCP tool contract testing verifies the server independently of the agent. A client discovers the available tools, binds typed arguments, invokes a known operation, and inspects the returned JSON. Invalid credentials or resource identifiers are also tested to ensure errors remain visible and actionable.

A successful build proves only that the server compiles. Independent invocation proves that process launch, transport, discovery, naming, authentication, argument handling, and result serialization work together. This separation makes it easier to distinguish a tool integration failure from a reasoning or workflow failure.

For reusable network tools, testing begins below MCP with direct wrapper calls for known devices, degraded BGP, down interfaces, and blocked configuration commands. The MCP server, transport, bridge, and browser are then tested in order. This layering distinguishes a network-policy defect from an MCP session failure or client integration problem and verifies structured errors as part of the public contract.

# References

[[agenticaifordevopsengineers.pdf]]

[[buildingaiagentsfornetworkoperations.pdf]]
