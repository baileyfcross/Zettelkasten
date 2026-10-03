2026-09-07 23:25

Status: #baby

Tags: [[Blender Keyframe Animation and Rigging]] [[Blender Character Animation Workflow]] [[Blender Animation Editors and Timing]]

# Blender Actions and Nonlinear Animation

An action stores a reusable collection of animation data. The Nonlinear Animation editor places actions as strips so completed motions can be arranged, repeated, and combined without rebuilding every keyframe.

This is useful for cycles and for assembling complex performance from smaller movements. A looped action can cover repeated behavior, while strip timing and influence determine how it interacts with other actions.

For a walk, the rig's in-place keyed motion can be stored as one action and pushed into an NLA strip. The strip can exclude a duplicate closing frame, repeat for multiple steps, and be scaled in time, while a separate object-level path controls travel through the scene.

The Action Editor exposes an object's named action and its F-curve channels. Pushing an action down places it in the NLA stack as a contributing strip, while stashing stores it as a non-contributing strip for later reuse. This shift changes the editing level from individual keys to whole motions, enabling actions to be layered, blended, and rearranged as units.

# References

[[blenderfordummies4thedition.pdf]]
[[learningblender3e.pdf]]
[[modelingandanimationusingblender.pdf]]
