2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Controls and Styling]]

# JavaFX Control Architecture

Most JavaFX widgets extend `Control`, which extends `Parent` and ultimately `Node`. Application code works with the control's public properties and methods, while skins and child nodes provide its visual implementation. Because every control is a node, it can participate in scene-graph layout, receive input events, and use transformations and effects.

The primary APIs are in `javafx.scene.control`; chart components live in `javafx.scene.chart`, and reusable cell implementations are in `javafx.scene.control.cell`. Common abstract bases make related controls consistent. `Labeled` supplies text, graphics, alignment, font, and wrapping behavior, while shared selection and focus models standardize navigation through advanced controls. This hierarchy connects the general [[JavaFX Scene Graph Hierarchy]] to specific widgets such as [[JavaFX Labeled and Toggle Controls]].

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
