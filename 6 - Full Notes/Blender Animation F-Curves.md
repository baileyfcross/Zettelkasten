2026-09-07 23:25

Status: #baby

Tags: [[Blender Keyframe Animation and Rigging]] [[Blender Animation Editors and Timing]]

# Blender Animation F-Curves

An f-curve, or function curve, describes how an animated value changes between keyed moments. Its horizontal dimension represents frames and its vertical dimension represents the value of the animated property.

The curve makes interpolation visible. A straight segment suggests a constant rate, while a curved transition can ease into or out of motion; changing the curve alters movement without replacing the key poses themselves.

Blender separates interpolation between keys from extrapolation beyond the first and last keys. Bezier handles shape local acceleration, easing modes offer characteristic transitions, and F-curve modifiers add non-destructive effects such as cycles. Because location, rotation, material, and other animated properties occupy separate curves, channel filtering and grouping are essential when a scene contains many simultaneous values.

# References

[[blenderfordummies4thedition.pdf]]
[[modelingandanimationusingblender.pdf]]
