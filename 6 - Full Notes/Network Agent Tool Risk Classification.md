2026-09-27 22:03

Status: #baby

Tags: [[Production Network Agent Operations]]

# Network Agent Tool Risk Classification

Network agent tool risk classification assigns an operational stance according to what a tool can affect. Device status and BGP summaries are relatively low-risk observations when scoped to approved devices. Constrained show commands need tighter review because their input surface is broader. Generic command execution, configuration changes, restarts, and session clears are high-risk capabilities.

The classification determines whether a call may run automatically, needs an approval record, or remains blocked. Narrow purpose-built tools are preferable to a broad `run_command` interface because their targets, arguments, output, and failure modes can be reviewed directly.

# References

[[buildingaiagentsfornetworkoperations.pdf]]
