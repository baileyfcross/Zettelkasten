2026-09-28 20:13

Status: #baby

Tags: [[Blender Game Asset Export]]

# Empty-Based Export Hierarchies

Blender empties can act as nonrenderable transform nodes in an exported hierarchy. Their positions, animation, and parent-child relationships provide attachment points or organizational roots even when the destination engine does not treat exported cameras and lights as equivalent native components.

A runtime object can be attached beneath the imported empty and inherit its stored transform or motion. The exporter must include empty objects, and the hierarchy should be tested because relation preservation is more dependable than application-specific behavior.

# References

[[howtocheatinblender27x.pdf]]
