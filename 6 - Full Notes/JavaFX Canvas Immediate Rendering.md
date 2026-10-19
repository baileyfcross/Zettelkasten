2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Graphics and 3D]]

# JavaFX Canvas Immediate Rendering

`Canvas` is a scene-graph node whose `GraphicsContext` issues drawing commands into a rendering buffer. Unlike shapes, which remain as individual nodes and are redrawn through retained-mode scene-graph optimization, canvas content is immediate mode: the application is responsible for repainting the buffer when its picture changes.

A canvas can be more efficient than hundreds or thousands of separate nodes for a complex dynamic drawing because it remains one node in the hierarchy. The tradeoff is that individual painted objects no longer have their own node properties, events, or automatic dirty-region management. The application must maintain its own model and map input coordinates back to that model. Repeated redraws are organized through [[JavaFX Canvas Animation Loop]].

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
