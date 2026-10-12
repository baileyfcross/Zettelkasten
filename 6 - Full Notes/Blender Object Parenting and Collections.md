2026-09-07 23:25

Status: #baby

Tags: [[Blender 3D Viewport and Object Operations]]

# Blender Object Parenting and Collections

Parenting creates a hierarchy in which child objects can inherit a parent's transformations. It lets different object types move as an organized unit without joining their data into one object.

Collections provide another form of organization by grouping scene elements for visibility, selection, and view-layer control. Parenting expresses dependency, while collections express membership; using both preserves individual editability in a complex scene.

The historical Game Engine example parents a camera to an actor after applying the actor's rotation and scale. The camera then inherits the actor's translation and turning, producing a following view while remaining a separate object whose relative offset can be positioned deliberately.

# References

[[blenderfordummies4thedition.pdf]]

[[introductiontoblender30.pdf]]

[[testdriveblender.pdf]]
