2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Application Architecture]]

# JavaFX Application Lifecycle

A conventional JavaFX application subclasses `javafx.application.Application`. The JavaFX runtime constructs the application object, creates the JavaFX Application Thread, supplies the primary stage, and invokes the overridden `start(Stage)` method. Application code builds the interface inside that lifecycle instead of constructing the top-level window before the platform starts.

The application normally creates a root node, places it in a [[JavaFX Stage and Scene|Scene]], attaches that scene to the supplied stage, and calls `show()`. This arrangement gives the runtime responsibility for bootstrapping the toolkit while leaving scene construction to the application. In REPL or library-oriented situations, the platform can instead be started explicitly before UI work is scheduled, as described in [[JavaFX ND4J and JShell Workflow]].

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
