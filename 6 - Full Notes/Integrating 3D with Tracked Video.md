2026-09-07 23:25

Status: #baby

Tags: [[Blender Motion Tracking]]

# Integrating 3D with Tracked Video

A tracked and oriented camera gives a Blender scene the perspective and movement of the recorded shot. Three-dimensional objects can then be placed against measured reference geometry so their position and scale match the footage.

Convincing integration also depends on recreating the shot's lighting and combining render and footage in the Compositor. Camera background images are visible only through the camera and provide the immediate visual reference during placement.

Gress's plate-matching examples make the next checks explicit: compare key and fill direction, adjust RGB black/white/gamma levels, and reproduce atmospheric contrast and moving grain at the element's depth. A camera match alone does not prevent a pasted-on appearance. See [[Plate Lighting Reference for CG]] and [[Matching Moving Film Grain]].

A practical Blender composite renders the character over transparency, receives contact shadows on a floor or shadow-catcher surface, and places that result over the Movie Clip with an Alpha Over node. Eevee and Cycles can share the final composite while using different techniques to isolate the floor's shadow contribution.

# References

[[blenderfordummies4thedition.pdf]]
[[digitalvisualeffectsandcompositing.pdf]]
[[learningblender3e.pdf]]
