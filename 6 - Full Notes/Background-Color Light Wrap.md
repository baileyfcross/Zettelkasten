2026-09-15 18:17

Status: #baby

Tags: [[CG Integration and Render Passes]]

# Background-Color Light Wrap

Light wrap softens the cutout look by letting nearby background colors appear at the foreground's edge. The book constructs an edge-limited matte from the foreground alpha, blurs the background color, and applies that color through the matte. This is not the same as placing a generic white glow around an object: the apparent light should be drawn from the actual plate and confined to the contact edge. The same edge isolation can help control color spill. See [[Alpha Channel as Compositing Matte]].

# References

[[digitalvisualeffectsandcompositing.pdf]]
