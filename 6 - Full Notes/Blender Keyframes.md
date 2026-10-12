2026-09-07 23:25

Status: #baby

Tags: [[Blender Keyframe Animation and Rigging]] [[Blender Character Animation Workflow]] [[Blender Animation Editors and Timing]]

# Blender Keyframes

A keyframe records a property's value at a particular frame. Creating another keyframe for the same property at a later time gives Blender two important states between which it can calculate change.

Keys can be inserted from the 3D Viewport or directly from many interface properties. They establish the poses or values the artist chooses; interpolation determines what happens between them.

For a character, a key can record selected rig controls or a coordinated whole-character pose through a keying set. Frame position defines timing, so the animator can revise when a pose occurs independently from the values stored in that pose.

Blender's interface distinguishes a property keyed on the current frame from an animated property whose value is currently interpolated or changed without a new key. Those color cues help reveal whether an edit has actually entered the animation. Semantic keyframe types such as Breakdown, Moving Hold, Extreme, and Jitter can further label the role a key plays without changing the value it stores.

The source's first animation records cube location at frames 1 and 60. Blender calculates the intervening positions, showing that the keys define selected states rather than every displayed frame. The same insertion mechanism can record location, rotation, scale, or another animatable property.

# References

[[blenderfordummies4thedition.pdf]]
[[learningblender3e.pdf]]
[[modelingandanimationusingblender.pdf]]

[[testdriveblender.pdf]]
