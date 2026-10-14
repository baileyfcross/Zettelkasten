2026-10-01 00:39

Status: #baby

Tags: [[3D Game Rendering]]

# Ray Trace Rendering

Ray tracing constructs an image by following an imaginary ray from the eye through each display pixel into the scene. The nearest surface intersection identifies the visible object and provides the point at which material, lighting, shadow, reflection, or transmission calculations can be evaluated.

Secondary rays can test whether a light source is occluded or continue along reflected and refracted directions. This makes global visibility effects more natural than in [[Scanline Rendering]], but the repeated intersection searches increase computation. Image quality and cost therefore depend strongly on the number of pixels, objects, lights, and secondary rays followed.

# References

[[mathematicsforcomputergraphicsandgameprogramming.pdf]]
