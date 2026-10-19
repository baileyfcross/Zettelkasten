2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Application Architecture]]

# JavaFX Coordinate and Layout Model

JavaFX uses a two-dimensional coordinate system whose origin is at the upper-left of a scene or local parent space. X values increase to the right and Y values increase downward. A node can be positioned in an absolute scene coordinate system while also participating in coordinates local to its parent. Three-dimensional scenes add a Z axis for depth.

Manual placement is possible, but layout parents are normally preferable because they respond to window resizing, child insertion and removal, and changes in preferred sizes. A plain `Group` manages children without laying them out, whereas layout panes apply explicit positioning and growth rules. Because local coordinate spaces nest with the scene graph, moving or transforming a parent changes how its descendants are presented without rewriting every child's coordinates. See [[JavaFX Layout Panes]] and [[JavaFX 3D Cameras]].

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
