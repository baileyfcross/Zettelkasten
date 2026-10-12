2026-09-20 23:34

Status: #baby

Tags: [[Game Physics and Collision]]

# Dynamic Collision Sweep

A dynamic collision sweep accounts for object motion across a time interval by testing a shape along its displacement rather than only at its starting and ending positions. It reduces tunneling when fast objects cross thin obstacles between frames.

Relative motion can turn a moving-versus-moving query into one shape swept against another. The earliest valid time of impact identifies where response should begin before the remaining motion is considered.

# References

[[gameprogrammingincplusplus.pdf]]
