2026-09-14 00:20

Status: #baby

Tags: [[Blender Editor Structure]]

# Blender Region Structure

`ARegion` is an instance of a sub-area within a Blender editor, such as a main window region, header, toolbar, or panel area. It stores linked-list membership, two-dimensional view state, window and redraw rectangles, dimensions, visibility, handler lists, and a pointer to its [[Blender Region Type Structure]].

Regions divide a [[Blender Screen Area Structure]] into smaller concerns that can draw and receive input independently. The [[Blender Region Event Routing]] process finds the region under an event, while [[Blender Region Draw Dispatch]] calls the function registered for its type.

# References

[[coreblenderdevelopment.pdf]]

