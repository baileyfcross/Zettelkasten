2026-09-14 00:20

Status: #baby

Tags: [[Blender Editor Structure]]

# Blender Screen Area Structure

`ScrArea` is the rectangular portion of a [[Blender Screen Structure]] occupied by one editor. It points to layout vertices, stores its bounding rectangle and editor type, connects persistent [[Blender SpaceLink Structure]] data with the runtime [[Blender SpaceType Structure]], and owns region and event-handler lists.

An area's type can change while its place in the screen remains. During event routing and drawing, Blender sets the area in the current context before descending into its [[Blender Region Structure]] objects, so editor callbacks see the correct spatial and application state.

# References

[[coreblenderdevelopment.pdf]]

