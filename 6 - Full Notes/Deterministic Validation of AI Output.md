2026-09-27 12:11

Status: #baby

Tags: [[AI Pipeline Engineering]] [[AI-Assisted Network Output Parsing]]

# Deterministic Validation of AI Output

Deterministic validation tests a model response before another workflow step can trust it. Checks may require a nonempty file, exact Markdown headings, bullets under every section, valid JSON, allowed enumeration values, bounded confidence scores, or domain-specific security and policy rules.

The validator must stay synchronized with the prompt contract. If the expected schema changes, the code that enforces it changes in the same reviewed revision. The model generates a candidate; ordinary code decides whether that candidate is structurally fit for downstream automation.

For network-agent output, validation extends from JSON syntax to operational meaning. Required interface and BGP fields, allowed states, numeric types, peer-count relationships, source grounding, and explicit unknowns can all be checked without a model. A final troubleshooting answer can also be tested against tool facts so it cannot report healthy BGP when `established_peers` is lower than `total_peers`.

# References

[[agenticaifordevopsengineers.pdf]]

[[buildingaiagentsfornetworkoperations.pdf]]
