2026-09-18 17:13

Status: #baby

Tags: [[Game Loop and Object Architecture]]

# Drawable Game Object

A drawable game object exposes a draw operation used during the output phase of the [[Game Loop]]. It contributes visible representation without implying that the object must also change its state every frame.

Keeping drawing separate from [[Updateable Game Object]] behavior lets the world maintain distinct lists and supports objects that are only simulated, only rendered, or both.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]
