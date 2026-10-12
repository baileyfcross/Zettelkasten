2026-09-14 00:55

Status: #baby

Tags: [[COMSOL Model Construction]] [[COMSOL Geometry Configuration]]

# COMSOL Global Parameters and Variables

Parameters name constant model inputs such as dimensions, material choices, source strengths, or ambient conditions. Variables name reusable expressions that may depend on coordinates, fields, or other definitions.

Replacing repeated numeric literals with descriptive names reduces editing errors and makes sensitivity studies explicit. Scope still matters: global definitions can serve the whole model, while component variables can refer to local geometry and physics quantities used by [[COMSOL Domain and Boundary Selections|selected entities]].

# References

[[cosmolheattransfermodels.pdf]]
[[geometrycreationandimport.pdf]]
