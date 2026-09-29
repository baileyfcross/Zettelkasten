2026-09-28 20:13

Status: #baby

Tags: [[Blender Efficient Modeling and Retopology]]

# Decimate Retopology Tradeoff

The Decimate modifier quickly reduces polygon count according to a ratio, making it useful for rough simplification and proxy geometry. It is not a substitute for deliberate edge flow: automatic collapse can produce irregular topology and invalidate existing UV layouts.

Decimation is therefore strongest when speed and overall silhouette matter more than deformation-ready loops or preserved mapping. A carefully authored low-resolution mesh remains preferable for animation and controlled game topology.

# References

[[howtocheatinblender27x.pdf]]
