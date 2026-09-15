2026-09-15 18:17

Status: #baby

Tags: [[Rotoscopy and Motion Tracking]]

# Four-Point Corner Pin Tracking

Tracking four corners of a planar region lets a replacement image deform with that region rather than merely translate, rotate, or scale. A corner-pin transform maps the four replacement corners onto their tracked locations, so a screen or sign can appear to follow perspective changes. The tracks should correspond to the same physical plane; points at different depths can make the warp inconsistent. This is a more expressive image-space match than [[One-Point and Two-Point Tracking]], but it is still not a 3D camera solve.

# References

[[digitalvisualeffectsandcompositing.pdf]]
