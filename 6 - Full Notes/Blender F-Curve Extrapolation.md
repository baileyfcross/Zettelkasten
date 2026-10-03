2026-10-02 18:09

Status: #baby

Tags: [[Blender Animation Editors and Timing]]

# Blender F-Curve Extrapolation

Blender F-curve extrapolation defines an animated property's behavior before its first keyframe and after its last. Constant extrapolation holds the endpoint value, while Linear extrapolation extends the slope implied by the first or last segment beyond the keyed interval.

Cyclic F-curve modifiers provide another option by repeating a keyed pattern non-destructively. The distinction from interpolation is important: interpolation controls movement between keys, whereas extrapolation controls the unkeyed time outside them. Selecting the behavior deliberately prevents an object from freezing, drifting indefinitely, or looping when a different endpoint behavior was intended.

# References

[[modelingandanimationusingblender.pdf]]
