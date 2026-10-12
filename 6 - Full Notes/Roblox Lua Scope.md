2026-10-04 16:30

Status: #baby

Tags: [[Roblox Gameplay Programming]]

# Roblox Lua Scope

Scope determines where a Roblox Lua variable or function can be accessed. A local declaration belongs to its enclosing block or function, while broader declarations are visible through a larger environment and are more likely to collide or be changed unexpectedly.

Keeping state local clarifies ownership and prevents unrelated scripts or callbacks from depending on hidden globals. When several scripts genuinely need the same behavior or data, [[Roblox ModuleScript]] gives that sharing an explicit interface. Scope therefore supports both correctness inside one script and clean boundaries between systems.

# References

[[robloxgamedevelopmentin24hours_theofficialrobloxguide.pdf]]

