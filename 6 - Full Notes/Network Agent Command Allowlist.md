2026-09-27 22:03

Status: #baby

Tags: [[Production Network Agent Operations]]

# Network Agent Command Allowlist

A network agent command allowlist permits only explicitly reviewed read-only commands or command patterns. A wrapper can accept known `show` operations while rejecting configuration mode, restart, session-clear, and other state-changing requests before backend execution.

Checking only that text begins with `show` is useful for a lab but is not a complete production policy. Vendor syntax, command chaining, arguments, output volume, caller role, and target device all affect risk. The policy decision and rejection reason should appear in the [[Network Agent Tool Audit Event]].

# References

[[buildingaiagentsfornetworkoperations.pdf]]
