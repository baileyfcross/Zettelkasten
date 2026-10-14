2026-09-28 21:55

Status: #baby

Tags: [[Blender Render Optimization and Compositing]]

# Cycles GPU Compute Rendering

Cycles can move path-tracing work from the CPU to a supported graphics processor. The workflow requires enabling a compatible backend in Blender's system preferences and selecting GPU Compute as the scene's Cycles device.

Hardware choice changes performance rather than the scene's artistic intent. CUDA or OptiX serves supported NVIDIA hardware and HIP serves supported AMD hardware in the Blender 3.0 setup described by the source; actual benefit depends on the available device and scene.

# References

[[introductiontoblender30.pdf]]
