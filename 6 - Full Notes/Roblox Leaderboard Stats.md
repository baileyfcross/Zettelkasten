2026-10-04 16:30

Status: #baby

Tags: [[Roblox Gameplay Programming]]

# Roblox Leaderboard Stats

Roblox's built-in player list can display values placed in a specially named leaderstats container under each Player. IntValue, StringValue, and related value objects inside that folder become visible statistics such as score, wins, level, or currency.

The displayed value is only the live representation, not automatically durable storage. Server code should own authoritative changes, and values that must survive leaving the game need to be loaded and saved through [[Roblox DataStore Persistence]]. Clear naming and bounded update logic keep the leaderboard useful rather than turning it into an uncontrolled interface to player state.

# References

[[robloxgamedevelopmentin24hours_theofficialrobloxguide.pdf]]

