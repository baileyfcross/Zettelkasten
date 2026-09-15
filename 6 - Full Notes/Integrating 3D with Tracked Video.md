2026-09-07 23:25

Status: #baby

Tags: [[Blender Motion Tracking]]

# Integrating 3D with Tracked Video

A tracked and oriented camera gives a Blender scene the perspective and movement of the recorded shot. Three-dimensional objects can then be placed against measured reference geometry so their position and scale match the footage.

Convincing integration also depends on recreating the shot's lighting and combining render and footage in the Compositor. Camera background images are visible only through the camera and provide the immediate visual reference during placement.

Gress's plate-matching examples make the next checks explicit: compare key and fill direction, adjust RGB black/white/gamma levels, and reproduce atmospheric contrast and moving grain at the element's depth. A camera match alone does not prevent a pasted-on appearance. See [[Plate Lighting Reference for CG]] and [[Matching Moving Film Grain]].

# References

[[blenderfordummies4thedition.pdf]]
[[digitalvisualeffectsandcompositing.pdf]]
