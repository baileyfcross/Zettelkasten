2026-09-07 23:25

Status: #baby

Tags: [[Blender Motion Tracking]]

# Blender Tracking Markers

A tracking marker identifies a distinctive group of pixels that Blender should follow from frame to frame. High-contrast corners or patches are useful, provided that they belong to a physical feature at one depth rather than an accidental crossing of separate objects.

Tracks must be evaluated because automatic motion estimates can drift when a feature blurs or changes. Accurate tracks can be locked, while failed markers should be corrected or removed before solving the camera.

# References

[[blenderfordummies4thedition.pdf]]
