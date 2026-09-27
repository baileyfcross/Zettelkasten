2026-09-27 12:11

Status: #baby

Tags: [[DevOps AI Governance]]

# Prompt Injection Defense in DevOps

DevOps workflows routinely ingest attacker-influenced text from pull-request bodies, code comments, logs, and issue discussions. If a model interprets embedded instructions as workflow authority, that content can redirect analysis, request secret exposure, or encourage unsafe actions.

Defense requires both input shaping and an instruction hierarchy. The workflow truncates and sanitizes untrusted fields, labels them as data, and gives the system prompt sole authority. Tools and permissions then limit what a compromised response could do. Prompt wording helps, but deterministic access controls provide the reliable boundary.

# References

[[agenticaifordevopsengineers.pdf]]
