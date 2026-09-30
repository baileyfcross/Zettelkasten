2026-09-07 23:25

Status: #baby

Tags: [[Blender Motion Tracking]]

# Consistent Lighting for Motion Tracking

Motion trackers depend on image features remaining recognizable between frames. Flicker, low-light noise, and automatic exposure changes alter pixel patterns and can cause a marker to lose its feature.

Footage should therefore be well lit with stable illumination and, where possible, a fixed aperture. Darkening or flicker can be added during compositing after the clean image has supplied dependable tracking data.

The same production record later supports integration. Shadow direction, softness, intensity, and color in the footage guide the Blender sun and world lighting; stable exposure makes those cues comparable across frames instead of forcing the tracker and compositor to compensate for uncontrolled capture changes.

# References

[[blenderfordummies4thedition.pdf]]
[[learningblender3e.pdf]]
