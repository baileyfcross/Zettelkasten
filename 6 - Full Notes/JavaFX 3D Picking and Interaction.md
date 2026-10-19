2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Graphics and 3D]]

# JavaFX 3D Picking and Interaction

JavaFX can use mouse and gesture events to manipulate a 3D scene. A drag handler can record the pointer's screen coordinates and the current rotation angles when a press begins, then convert later coordinate differences into rotations around the X and Y axes. Grouping geometry beneath a transformed parent rotates the model as a unit.

Picking reports what a pointer ray intersects through `PickResult`, including the selected node and intersection details used by mouse, context-menu, drag, rotate, and scroll events. This allows object selection and position-aware interaction even though [[JavaFX 3D Cameras]] have projected the world onto a flat screen. Standard JavaFX event handling therefore extends naturally from controls to the shapes and meshes in [[JavaFX 3D Shapes and Meshes]].

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
