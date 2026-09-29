2026-09-28 21:55

Status: #baby

Tags: [[Blender Render Optimization and Compositing]]

# Cycles Noise-Threshold Sampling

Cycles adaptive sampling can stop refining pixels after their estimated noise falls below a threshold. Minimum and maximum sample limits bound the process, while a lower threshold asks the renderer to tolerate less residual noise.

This allocates work according to image difficulty rather than forcing every pixel to receive the same sample count. Smooth regions can finish early while noisy reflections or indirect-light regions continue sampling.

# References

[[introductiontoblender30.pdf]]
