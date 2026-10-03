2026-09-07 23:25

Status: #baby

Tags: [[Blender Keyframe Animation and Rigging]] [[Blender Character Animation Workflow]] [[Blender Animation Editors and Timing]]

# Blender Keying Sets

A keying set groups properties that should receive keyframes together. Built-in sets such as location, rotation, and scale reduce the chance that one related channel will be overlooked.

Custom keying sets can coordinate properties spread across objects, constraints, materials, and other editors. They are especially useful for complex rigs whose animation controls would otherwise require many separate keying actions.

A whole-character set can key the rig without manually selecting every control, while a custom facial set can restrict a keying action to expression controls. The active set should match the current task so convenience does not produce dense, unrelated keys across the performance.

In Blender's Timeline, the active keying set determines which properties the insert and delete key controls affect at the current frame. Auto-keyframing can also operate through that set. The set is therefore both a convenience and a recording boundary: it defines what a single timing decision means across otherwise separate animation channels.

# References

[[blenderfordummies4thedition.pdf]]
[[learningblender3e.pdf]]
[[modelingandanimationusingblender.pdf]]
