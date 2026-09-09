2026-09-08 09:04

Status: #baby

Tags: [[Procedural Mesh Editing with bmesh]]

# bmesh Transform Operations

BMesh selection and Blender transform operators work together: the script identifies mesh components through `bmesh`, then translation, rotation, scaling, or related Edit Mode operators act on that selected subset. This combines explicit topology access with familiar high-level operations.

The outcome depends on coordinate space, pivot behavior, and the current Edit Mode context. For precise algorithms, selection should be established from geometric criteria and the transform should state its intended displacement or constraint. This separates the question of which components are affected from the question of how they move.

# References

[[blenderpythonapi.pdf]]
