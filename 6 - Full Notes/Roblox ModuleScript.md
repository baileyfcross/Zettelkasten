2026-10-04 16:30

Status: #baby

Tags: [[Roblox Gameplay Programming]]

# Roblox ModuleScript

A ModuleScript returns a value, commonly a table of related functions and data, when another script calls require. It packages reusable logic behind one interface so multiple systems do not need copied implementations.

Placement defines availability: a server-only module can live in ServerStorage, while code legitimately needed by both server and client can be placed in ReplicatedStorage. Module dependencies should remain acyclic because circular requires can prevent initialization from completing. Combined with [[Roblox Lua Scope]], modules make shared state and capabilities explicit.

# References

[[robloxgamedevelopmentin24hours_theofficialrobloxguide.pdf]]

