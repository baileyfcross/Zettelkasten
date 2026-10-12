2026-09-14 00:20

Status: #baby

Tags: [[Blender Editor Construction]]

# Blender UI Button

A core Blender UI button is created through the interface API with a control type, identifier, label, location, dimensions, optional data pointer, numeric bounds, auxiliary values, and tooltip. The returned runtime object belongs to a [[Blender UI Block]] that coordinates the surrounding controls.

In the tutorial editor, the button does not keep an independent value; its purpose is to invoke an operation that changes the main region. [[Blender Editor Button Operator Binding]] stores the corresponding operator type so an ordinary interface event reaches the correct poll and execution callbacks.

# References

[[coreblenderdevelopment.pdf]]

