2026-10-02 18:09

Status: #baby

Tags: [[Blender 3D Viewport and Object Operations]]

# Blender Snapping

Blender snapping constrains a transformation to meaningful scene elements instead of leaving placement entirely continuous. Increment snapping follows grid points, while vertex, edge, and face modes attach the transformed selection to corresponding mesh components. Volume snapping uses the region inside an object beneath the pointer to control depth.

The appropriate target depends on the relationship being built: grid increments support measured layouts, vertices and edges support exact topology alignment, and faces or volumes support surface placement. Snapping works alongside [[Transform Orientations in Blender]] and [[Blender Transform Pivot Points]], so accurate placement depends on both the target and the frame in which the transform is interpreted.

# References

[[modelingandanimationusingblender.pdf]]
