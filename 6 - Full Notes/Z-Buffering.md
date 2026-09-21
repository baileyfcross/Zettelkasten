2026-09-18 17:13

Status: #baby

Tags: [[3D Game Rendering]]

# Z-Buffering

Z-buffering stores the nearest depth written for each screen pixel. A new fragment is displayed only if its depth test shows that it is closer than the value already stored, after which the buffer is updated.

This per-pixel visibility method removes the need to sort every three-dimensional surface with a painter's algorithm. The depth buffer is cleared along with the color buffer before rendering a new frame.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]
