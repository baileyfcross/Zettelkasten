2026-09-27 18:30

Status: #baby

Tags: [[AI-Assisted Network Security]]

# Multi-Vendor Firewall Log Normalization

Multi-vendor firewall log normalization maps different textual formats into a common event schema. Cisco ASA and pfSense records may express action, protocol, source, destination, ports, interface, and reason in different positions and conventions.

Normalization preserves the original line while extracting comparable fields and identifying the parser used. Unsupported or malformed input should be marked, not forced into misleading defaults. Once events share a schema, detection logic can compare patterns across vendors without depending on one product's formatting.

# References

[[ainetworkingcookbook.pdf]]
