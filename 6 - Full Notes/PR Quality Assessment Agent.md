2026-09-27 12:11

Status: #baby

Tags: [[DevOps Agent Safety and Autonomy]]

# PR Quality Assessment Agent

A PR quality assessment agent reviews a compact changed-file inventory, identifies high-risk candidates, and retrieves only targeted diffs when deeper evidence is needed. It returns a JSON summary with overall risk, concrete issues, file locations, categories, suggested small fixes, missing tests, and confidence.

The agent treats diff content as untrusted, cannot access the repository or shell broadly, and cannot paste code or suggest destructive commands. A deterministic validator checks the schema, while a separate risk gate may fail the workflow only when high risk and sufficient confidence meet explicit policy.

# References

[[agenticaifordevopsengineers.pdf]]
