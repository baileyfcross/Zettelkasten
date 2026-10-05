2026-10-04 16:30

Status: #baby

Tags: [[Roblox Gameplay Programming]]

# Roblox TeleportService

TeleportService moves players between Roblox places or servers. It supports experience structures in which a starting lobby, match, dungeon, or other level is a separate destination rather than another region in the same loaded place.

In-place movement can use a character's [[Roblox CFrame Transform]], but cross-place travel requires a published destination and must be tested under live platform conditions. Teleport code should handle failure and preserve the player context needed on arrival. The service is therefore the runtime connection between the levels described by [[Roblox Place Structure]].

# References

[[robloxgamedevelopmentin24hours_theofficialrobloxguide.pdf]]

