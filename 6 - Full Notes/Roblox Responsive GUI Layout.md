2026-10-04 16:30

Status: #baby

Tags: [[Roblox Gameplay Programming]]

# Roblox Responsive GUI Layout

Roblox GUI positions and sizes can combine Scale, which is proportional to the parent, with Offset, which is measured in pixels. Scale-heavy layouts adapt naturally to different resolutions, while fixed offsets are useful for details that should retain a specific size.

Layout objects and constraints can arrange children, preserve aspect ratios, and limit sizes. A UIScale can resize a whole interface subtree consistently. Responsive authoring should be tested on more than one device profile, because a layout that fits a desktop viewport may overlap touch controls or become unreadable on mobile. See [[Roblox Mobile UI Compatibility]].

# References

[[robloxgamedevelopmentin24hours_theofficialrobloxguide.pdf]]

