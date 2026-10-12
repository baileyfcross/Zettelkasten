2026-09-28 21:55

Status: #baby

Tags: [[Blender Render Optimization and Compositing]]

# Cycles Denoising Workflow

Denoising estimates a clean image from a noisy low-sample render. Blender can denoise during viewport or final rendering, and the Compositor can apply a Denoise node after rendering from the image and auxiliary denoising data.

The operation can shorten iteration by making fewer samples usable, but it does not recover arbitrary detail that sampling never captured. Sampling level and denoising should therefore be tuned together and checked for lost texture or softened edges.

# References

[[introductiontoblender30.pdf]]
