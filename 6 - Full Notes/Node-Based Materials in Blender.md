2026-09-07 23:25

Status: #baby

Tags: [[Blender Materials and Textures]] [[Blender Image and Shader Editing]]

# Node-Based Materials in Blender

A node-based material expresses surface appearance as a network of connected operations. The Shading workspace pairs a rendered material preview in the 3D Viewport with the Shader Editor where the network is built.

A basic material connects a Principled BSDF shader to Material Output. The output node maps the network's result onto the object; without a material output, the renderer has no final surface description to use.

Nodes communicate through typed input and output sockets. Image and procedural textures generate data, mapping and conversion nodes transform it, shader nodes describe light response, and Material, Light, or World Output nodes terminate the appropriate graph. Node groups can encapsulate a coordinated portion of this network, reducing clutter while keeping its internal calculation editable.

# References

[[blenderfordummies4thedition.pdf]]

[[introductiontoblender30.pdf]]

[[modelingandanimationusingblender.pdf]]
