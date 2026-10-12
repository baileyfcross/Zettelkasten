2026-09-15 18:17

Status: #baby

Tags: [[Particle and Destruction VFX]]

# Rigid Body Fracture and Collision

A rigid-body solver moves hard pieces that retain their shapes while colliding under specified forces. To destroy a solid-looking building in the book's example, the model is first fractured into separate parts, then a non-rendering collision object is driven into it. The solver sends the fragments apart, but their visual suitability still depends on the fracture design, materials, timing, and motion blur. A full intact model can be shown until the moment it is swapped for the fractured version. See [[Choreographing Destruction Layers]].

# References

[[digitalvisualeffectsandcompositing.pdf]]
