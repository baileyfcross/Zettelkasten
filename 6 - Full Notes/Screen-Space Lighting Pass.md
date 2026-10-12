2026-09-20 23:34

Status: #baby

Tags: [[Advanced Real-Time Rendering]]

# Screen-Space Lighting Pass

A screen-space lighting pass reads surface properties from a [[G-Buffer]] and calculates illumination for the pixels covered by a light. Global lights can use a full-screen shape, while a point light can render geometry approximating its region of influence.

Additive blending accumulates contributions from multiple lights. Depth and stencil techniques can limit work and address cases where light volumes cross surfaces or contain the camera.

# References

[[gameprogrammingincplusplus.pdf]]
