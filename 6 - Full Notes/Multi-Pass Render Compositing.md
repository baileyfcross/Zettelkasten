2026-09-15 18:17

Status: #baby

Tags: [[CG Integration and Render Passes]]

# Multi-Pass Render Compositing

Instead of baking every CG contribution into one beauty image, a renderer can output separate color, diffuse, specular, individual-light, shadow, luminosity, normal, and depth passes. A compositor combines them with appropriate merges, blend modes, and mattes. This lets light contributions or surface appearance be adjusted after rendering without repeating a costly scene render. The amount of control depends on which quantities were actually separated: a lighting pass with a baked surface cannot offer the same retexturing freedom as a dedicated surface pass. See [[Layer-Based and Node-Based Compositing]].

# References

[[digitalvisualeffectsandcompositing.pdf]]
