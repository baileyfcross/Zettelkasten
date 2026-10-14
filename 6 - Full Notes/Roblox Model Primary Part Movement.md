2026-10-04 16:30

Status: #baby

Tags: [[Roblox Gameplay Programming]]

# Roblox Model Primary Part Movement

A Roblox Model groups instances but does not itself have the same position and orientation properties as a BasePart. Assigning a PrimaryPart gives the model a reference part whose transform can be used to move the assembly as a coherent unit.

The remaining parts must maintain their intended relationship to that reference, typically through welding or a stable hierarchy. Setting the model through its primary transform is more reliable than independently repositioning every child. The target pose is commonly expressed as a [[Roblox CFrame Transform]] and can be animated through code or [[Roblox TweenService]].

# References

[[robloxgamedevelopmentin24hours_theofficialrobloxguide.pdf]]

