2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Application Architecture]]

# JavaFX Scene Graph Hierarchy

The JavaFX scene graph is a strictly hierarchical collection of `Node` objects beneath a scene's root. Every node except the root has exactly one parent. A node can appear only once in a scene graph unless it is first removed from its previous location. Parent nodes contain and arrange children, while leaves such as shapes and image views contain no child nodes.

Only nodes attached to the graph participate in that scene's rendering. The hierarchy also lets transformations, styles, and layout decisions apply through nested structures. A control is ultimately a node, so it inherits effects, scaling, rotation, input handling, and placement behavior even when its public API presents a higher-level widget. The hierarchy underpins [[JavaFX Coordinate and Layout Model]], [[JavaFX Control Architecture]], and retained-mode rendering in contrast with [[JavaFX Canvas Immediate Rendering]].

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
