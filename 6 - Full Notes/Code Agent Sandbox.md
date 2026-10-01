2026-09-30 17:53

Status: #baby

Tags: [[Code LLM Development Workflows]]

# Code Agent Sandbox

A code agent sandbox is an isolated execution environment in which generated code, build commands, and tests can run without unrestricted access to production systems or developer credentials. It contains the blast radius of incorrect or hostile output.

The sandbox should define filesystem, network, process, time, and resource limits and start from a reproducible project state. Results and artifacts return to the agent as evidence, while promotion outside the sandbox remains a separate reviewed action.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]
