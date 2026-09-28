2026-09-27 18:30

Status: #baby

Tags: [[Network Copilot Design]]

# Conversation-Aware Network Context

Conversation-aware network context retains relevant earlier exchanges so a follow-up such as “what about the backup link?” can be interpreted against the device and problem already under discussion. This makes the copilot feel continuous rather than forcing every prompt to restate the full case.

History should be bounded and summarized because an ever-growing transcript adds cost, stale assumptions, and conflicting instructions. The copilot should distinguish conversational claims from authoritative device data. A retained answer from the model is context for dialogue, not verified network state.

Application-managed memory implements this distinction by storing user and assistant turns and deliberately rebuilding the next prompt. Full history fits a short lab; recent-window or summary memory better serves a long incident. Tool results can enter the active context so follow-up questions remain coherent, but they should also stay in a structured evidence store that can be validated independently of the conversation.

# References

[[ainetworkingcookbook.pdf]]

[[buildingaiagentsfornetworkoperations.pdf]]
