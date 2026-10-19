2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Deployment and Platform Integration]]

# JavaFX Migration with JFXPanel and SwingNode

JavaFX supports incremental Swing migration in both directions. `JFXPanel` places a complete JavaFX scene inside an existing Swing component hierarchy, making it suitable for introducing capabilities such as WebView or JavaFX 3D without rewriting the whole application. `SwingNode` places a Swing component inside a JavaFX scene when a legacy library or specialized widget must remain.

A practical migration begins by identifying separable Swing regions and replacing them one at a time with JavaFX scenes. As converted regions grow, several panels can be regrouped into larger JavaFX hierarchies. Remaining Swing components can be wrapped with `SwingNode`, so migration does not require a single disruptive cutover. The architectural flexibility does not remove the dual-thread constraint in [[JavaFX and Swing Integration Threads]].

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
