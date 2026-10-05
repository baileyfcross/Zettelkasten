2026-10-04 16:30

Status: #baby

Tags: [[Roblox Gameplay Programming]]

# Roblox Collision Fidelity

Collision fidelity controls how closely a Roblox mesh or union's physical collision shape follows its visible geometry. Simpler approximations such as boxes or hulls are cheaper to simulate, while precise convex decomposition can better match complex shapes at a higher runtime cost.

The most detailed option is not automatically the best. Background geometry and large numbers of objects often benefit from simple collision, and invisible primitive parts can provide predictable walkable or blocking surfaces around a detailed mesh. This tradeoff links world construction to [[Roblox Cross-Platform Performance Optimization]].

# References

[[robloxgamedevelopmentin24hours_theofficialrobloxguide.pdf]]

