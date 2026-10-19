2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Reactive UI Composition]]

# Scene Builder FXML Workflow

Scene Builder is a visual editor that reads and writes FXML. It presents palettes of JavaFX layouts and controls, a hierarchy view of the scene graph, and property panels for the selected element. A developer can drag an image view, pane, text, or effect into the hierarchy and save the resulting changes directly to the project's FXML file.

The tool accelerates interface composition without replacing the application's Java model or controller. Because FXML is the intermediate format, the saved result remains editable as text, loadable by the normal JavaFX runtime, and compatible with stylesheets. Scene Builder is therefore a view-authoring companion to [[FXML View Definition]] rather than a separate runtime, and the controller remains connected through [[FXML Controller Wiring]].

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
