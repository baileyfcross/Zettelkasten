2026-10-04 16:30

Status: #baby

Tags: [[Roblox Gameplay Programming]]

# Roblox Touched Event Debouncing

A part's Touched event can fire repeatedly while bodies make, break, or multiply their contacts. If the handler awards points, deals damage, or starts an expensive action on every signal, one apparent collision may trigger the result many times.

A debounce records whether the action is already active or was recently handled, ignores duplicate signals during that interval, and resets only when another activation is allowed. The exact reset policy should match the mechanic: cooldowns, one-time pickups, and per-character hazards need different state. Debouncing turns raw collision notifications into deliberate gameplay events.

# References

[[robloxgamedevelopmentin24hours_theofficialrobloxguide.pdf]]

