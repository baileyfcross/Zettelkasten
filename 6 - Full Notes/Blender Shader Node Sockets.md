2026-10-02 18:09

Status: #baby

Tags: [[Blender Image and Shader Editing]]

# Blender Shader Node Sockets

Blender shader node sockets are the typed connection points through which a material graph exchanges information. Input sockets appear on the left of a node and accept values or links; output sockets appear on the right and provide a node's result. Their type indicates whether they carry a scalar, vector, color, or shader closure.

Linking an output to a compatible input replaces or drives the input's local value. This makes the graph's dataflow explicit: coordinates feed textures, textures feed color or scalar controls, and shaders feed mix or output nodes. Understanding socket direction and type prevents a visually connected graph from being mistaken for a semantically valid one.

# References

[[modelingandanimationusingblender.pdf]]
