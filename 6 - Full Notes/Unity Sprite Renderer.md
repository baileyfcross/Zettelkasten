2026-10-12 01:03

Status: #baby

Tags: [[Unity 2D Interface and Mobile Development]]

# Unity Sprite Renderer

A Unity Sprite Renderer displays a sprite in a scene and controls presentation properties such as tint, flipping, sorting layer, and order within that layer. In a typical 2D project it provides the visible component for a flat image-based object.

Sprites still occupy a scene with transforms and cameras, but their draw order should be explicit. Combining the renderer with a [[Unity Sorting Layer]] avoids relying accidentally on z position, while [[Unity 2D Physics]] components can supply collision and motion independently of the visible sprite.

# References

[[unitygamedevelopmentin24hourssamsteachyourself4e.pdf]]

