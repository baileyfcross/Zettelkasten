2026-09-14 01:18

Status: #baby

Tags: [[Blender Texture Painting Workflow]]

# Texture Paint Bleed and Occlusion

Texture-paint bleed extends color slightly beyond a face's UV boundary so filtering does not reveal an unpainted seam. The margin should cover expected mipmap and sampling behavior without contaminating nearby islands.

Occlusion, backface, and normal-related options control whether the brush reaches surfaces hidden or turned away from the view. Enabling them appropriately prevents a stroke on the visible side from leaking through to unrelated geometry.

# References

[[creatinggameenvironmentsinblender3d.pdf]]

