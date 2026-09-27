2026-09-27 18:30

Status: #baby

Tags: [[Network Copilot Design]]

# Network Copilot Intent Classification

Network copilot intent classification maps a user's question to a task category such as configuration, troubleshooting, explanation, or status inquiry. Even a simple keyword method can choose a more relevant prompt structure and determine which context or tool the copilot should use.

Classification should expose uncertainty and allow correction because the same term can appear in several intents. A question that mentions “configure” might ask for an explanation rather than a change. The classified intent guides the [[Network Copilot Response Pipeline]] but should not grant operational authority.

# References

[[ainetworkingcookbook.pdf]]
