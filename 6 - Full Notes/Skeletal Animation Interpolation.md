2026-09-20 23:34

Status: #baby

Tags: [[Skeletal Animation Systems]]

# Skeletal Animation Interpolation

Skeletal animation interpolation constructs a pose between two sampled animation frames. Translation is blended linearly, while rotation uses quaternion interpolation so orientation follows a meaningful path without Euler-angle discontinuities.

The same fraction must be applied across corresponding bones to produce a coherent pose. Interpolation smooths playback when the render or update rate differs from the stored [[Animation Clip]] sampling rate.

# References

[[gameprogrammingincplusplus.pdf]]
