2026-10-01 00:39

Status: #baby

Tags: [[OpenGL Rendering Pipeline]]

# OpenGL as State Machine

OpenGL retains rendering state such as the current color, point size, line width, background clear color, matrix mode, and enabled capabilities. Once a command changes a state value, subsequent drawing commands use it until another command replaces it.

This design keeps individual vertex specifications compact but makes output depend on the sequence of earlier calls. A drawing routine must therefore establish the state it relies on or deliberately inherit it. State changes and geometry submission together form a command stream rather than a self-contained scene description.

# References

[[mathematicsforcomputergraphicsandgameprogramming.pdf]]
