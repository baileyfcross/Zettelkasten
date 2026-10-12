2026-09-27 22:03

Status: #baby

Tags: [[AI-Assisted Network Output Parsing]]

# Network CLI Structured Extraction

Network CLI structured extraction converts unstructured command output into a deliberately small object that downstream code can parse and validate. The prompt identifies the command context and exact fields, the model proposes JSON, and ordinary code checks that proposal before use. This makes the model useful for irregular text without confusing fluent interpretation with authoritative device state.

The result should contain only facts supported by the raw output. Missing fields become `null` or an explicit unknown state rather than a plausible invention, and the original CLI text remains available for audit and troubleshooting.

# References

[[buildingaiagentsfornetworkoperations.pdf]]
