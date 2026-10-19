2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Web Cloud and Data Applications]]

# JavaFX ND4J and JShell Workflow

ND4J presents N-dimensional linear algebra through Java APIs while selecting an optimized native implementation for the operating system and available CPU or GPU. When started with the project's classpath, JShell can import ND4J, create arrays and matrices, and return each result immediately, supporting exploratory scientific calculation without a complete application cycle.

JavaFX can run in the same REPL because JShell executes on a JVM. `Platform.startup` initializes the toolkit, and later scene-graph work is scheduled with `Platform.runLater`. Reusable compiled helper functions make this practical: a function can accept numeric arrays and a title, create a scatter chart, and show it from a short JShell statement. The workflow joins rapid numeric experimentation with [[JavaFX Scientific Visualization]].

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
