2026-09-27 18:30

Status: #baby

Tags: [[Network Copilot Design]]

# Device-Aware Copilot State

Device-aware copilot state records which router, switch, or firewall is the current subject of a conversation. The selected device can supply vendor, model, address, protocols, and role so later questions receive platform-specific answers without repeating every attribute.

The state must be explicit and changeable because an unnoticed device switch can apply correct syntax to the wrong target. Before presenting commands, the copilot should identify the device context it used. Inventory remains authoritative; conversational selection only points to the relevant record.

# References

[[ainetworkingcookbook.pdf]]
