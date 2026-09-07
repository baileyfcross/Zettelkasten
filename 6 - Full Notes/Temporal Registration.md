2026-09-06 21:16

Status: #baby

Tags: [[Spatial Tracking and Registration]]

# Temporal Registration

Temporal registration aligns measurements, simulation state, rendering, and display output to compatible moments in time. Without it, correctly calibrated virtual geometry can lag behind a moving camera or object and appear spatially misplaced.

Timestamps help synchronize sensors with different rates, while prediction can estimate the pose expected when the generated image reaches the display. Variable or unknown latency makes this compensation more difficult.

# References

[[augmentedreality_pearson.pdf]]
