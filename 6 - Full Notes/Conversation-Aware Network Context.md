2026-09-27 18:30

Status: #baby

Tags: [[Network Copilot Design]]

# Conversation-Aware Network Context

Conversation-aware network context retains relevant earlier exchanges so a follow-up such as “what about the backup link?” can be interpreted against the device and problem already under discussion. This makes the copilot feel continuous rather than forcing every prompt to restate the full case.

History should be bounded and summarized because an ever-growing transcript adds cost, stale assumptions, and conflicting instructions. The copilot should distinguish conversational claims from authoritative device data. A retained answer from the model is context for dialogue, not verified network state.

# References

[[ainetworkingcookbook.pdf]]
