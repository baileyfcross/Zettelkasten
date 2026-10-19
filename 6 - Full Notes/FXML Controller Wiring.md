2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Reactive UI Composition]]

# FXML Controller Wiring

An FXML controller supplies behavior for a declaratively defined view. The FXML document identifies the controller class, gives selected nodes `fx:id` names, and maps event attributes to controller methods. Fields and methods marked for FXML injection let the loader connect the constructed scene graph to the code that responds to it.

This arrangement keeps layout and visual composition in [[FXML View Definition]] while the controller coordinates actions, selection, and model updates. A controller can bind a button's disabled property to observable form state, listen for changes in a list selection, or implement create, delete, and update handlers. Because injected controls become part of a live scene, all controller-driven UI changes must respect the [[JavaFX Application Thread]].

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
