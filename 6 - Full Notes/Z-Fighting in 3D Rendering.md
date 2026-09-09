2026-09-08 09:04

Status: #baby

Tags: [[Portable 3D Model Data]]

# Z-Fighting in 3D Rendering

Z-fighting occurs when two surfaces occupy the same or nearly the same depth and compete for the renderer's depth-buffer decision. Small floating-point differences cause fragments from each surface to appear inconsistently, producing flicker or noisy patterns.

The durable solution is to remove the geometric ambiguity. One surface can be offset slightly, an unnecessary interior face can be deleted, or coplanar topology can be dissolved and rebuilt. Changing render settings may alter the symptom, but correcting overlapping geometry makes the model more portable across renderers.

# References

[[blenderpythonapi.pdf]]
