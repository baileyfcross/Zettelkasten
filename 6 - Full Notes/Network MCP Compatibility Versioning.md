2026-09-27 22:03

Status: #baby

Tags: [[Network MCP Tool Architecture]]

# Network MCP Compatibility Versioning

Network MCP compatibility versioning treats a public tool’s name, arguments, result shape, and error shape as a dependency shared by its clients. Once a browser, assistant, or automation service relies on `bgp_summary(device)`, casually renaming a field or changing its type can break every consumer even if the internal wrapper still works.

Implementation details may evolve behind the contract, but breaking interface changes should use an explicit version or new tool name. [[MCP Tool Contract Testing]] then verifies both successful calls and controlled failures against each supported contract.

# References

[[buildingaiagentsfornetworkoperations.pdf]]
