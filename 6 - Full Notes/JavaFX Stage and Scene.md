2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Application Architecture]]

# JavaFX Stage and Scene

JavaFX uses a theater metaphor for its top-level display structure. A `Stage` is the host window supplied by the platform in a desktop application. A `Scene` is the container installed in that stage, and the scene owns a root node from which the visible hierarchy begins. The stage can be titled, decorated or undecorated, assigned a scene, and shown after the hierarchy is ready.

This separation matters because windows, rendered content, and individual interface elements have different responsibilities. A complete scene can also be embedded inside Swing through a `JFXPanel`; individual JavaFX nodes are not inserted directly into the Swing component tree. Within JavaFX, the scene delegates its visual structure to the [[JavaFX Scene Graph Hierarchy]] and its layout behavior to [[JavaFX Layout Panes]].

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
