2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Controls and Styling]]

# JavaFX CSS Selectors and Application

JavaFX CSS applies presentation properties to nodes through selectors based on built-in style classes, custom style classes, object IDs, descendant relationships, and supported pseudo-classes. Java-style camel-case properties appear in CSS as hyphenated names prefixed with `-fx-`. Stylesheets can be attached to a scene or to a `Parent`, where their scope covers that node and its descendants.

Multiple stylesheets can contribute to a scene, and inline `setStyle` declarations can change a node dynamically. JavaFX partially supports unconditional `@import`, and supported pseudo-classes are defined by each node rather than by the complete web CSS standard. These mechanisms separate presentation from control logic and prepare reusable themes described in [[JavaFX CSS Themes Paints and Effects]].

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
