2026-10-02 18:09

Status: #baby

Tags: [[Blender Image and Shader Editing]]

# Blender Shader Node Groups

Blender shader node groups package a selected subgraph as one reusable node with an exposed interface. Grouping reduces visual clutter and gives a meaningful boundary to a repeated material operation, while the internal nodes continue to perform the underlying texture, conversion, and shader work.

The group can be entered for detailed editing and the parent node tree restores the surrounding graph. Its usefulness depends on choosing inputs and outputs that express a coherent operation; hiding arbitrary complexity without a clear interface only moves confusion inward. Groups are especially valuable when the same coordinated shader logic appears across several materials.

# References

[[modelingandanimationusingblender.pdf]]
