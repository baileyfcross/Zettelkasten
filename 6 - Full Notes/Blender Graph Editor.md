2026-09-07 23:25

Status: #baby

Tags: [[Blender Keyframe Animation and Rigging]] [[Blender Character Animation Workflow]] [[Blender Animation Editors and Timing]]

# Blender Graph Editor

The Graph Editor displays animated properties as curves across time. It is the primary place for final polish after the broad poses and timing of an animation have been blocked and refined.

Its interaction resembles the 3D Viewport: points can be selected, moved, scaled, duplicated, or aligned by frame. Editing handles and curve shapes changes the rate and character of motion between keys rather than only the keys' values.

Each animated channel has its own F-curve, whose horizontal dimension is time and vertical dimension is value. Linear and eased curves can connect the same two poses but produce constant or changing speed; normalization and selected-curve filtering help compare channels with very different numerical ranges.

The editor also exposes extrapolation, handle types, easing, snapping, curve baking, smoothing, and F-curve modifiers. Ghost curves preserve a visual snapshot for comparison, while error and selection filters narrow the visible channel set. This makes the Graph Editor both a curve-shaping tool and a diagnostic surface for understanding why an animated property moves as it does.

# References

[[blenderfordummies4thedition.pdf]]
[[learningblender3e.pdf]]
[[modelingandanimationusingblender.pdf]]
