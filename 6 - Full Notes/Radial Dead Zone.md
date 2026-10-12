2026-09-20 23:34

Status: #baby

Tags: [[Game Input Systems]]

# Radial Dead Zone

A radial dead zone filters a two-dimensional analog stick according to the magnitude of its vector rather than filtering the horizontal and vertical axes independently. Values inside a central radius become zero.

Values outside the dead zone are rescaled so movement reaches full magnitude near the hardware limit. This preserves circular direction behavior and avoids the square or cross-shaped response created by separate axis thresholds.

# References

[[gameprogrammingincplusplus.pdf]]
