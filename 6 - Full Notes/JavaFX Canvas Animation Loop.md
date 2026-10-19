2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Graphics and 3D]]

# JavaFX Canvas Animation Loop

An animated canvas application separates one-time setup from repeated model updates and drawing. The book's graphics skeleton controls draw frequency with a `Timeline` and a frame-duration derived from a requested frames-per-second value. Each draw callback receives a `GraphicsContext`, clears or repaints the canvas, and can read input registered on the canvas node.

This loop is appropriate when many visual elements are represented as ordinary model objects rather than scene-graph nodes. A bouncing-ball or simulation frame updates positions and then redraws their current state. Frame scheduling does not make expensive computation free: rendering remains constrained by the [[JavaFX Application Thread]], so costly preparation should follow [[JavaFX Graphics Threading and Performance]].

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
