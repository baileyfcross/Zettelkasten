2026-09-07 23:25

Status: #baby

Tags: [[Blender Keyframe Animation and Rigging]] · [[Blender Efficient Modeling and Retopology]]

# Blender Hooks

A hook binds selected vertices or control points to another object, commonly an Empty, through a Hook modifier. Transforming the controller then deforms the assigned points.

Hooks provide looser and more directional control than predefined shape keys. They are useful for broad organic deformation and for animating curve control points, and their influence can be adjusted in the modifier.

Creating a hook from selected vertices can generate an Empty controller and a configured Hook modifier. The modifier's radius and falloff shape distribute the controller's influence, while transforming or keyframing the Empty provides nondestructive object-level control over those mesh vertices.

# References

[[blenderfordummies4thedition.pdf]]

[[howtocheatinblender27x.pdf]]
