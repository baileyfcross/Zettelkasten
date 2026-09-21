2026-09-18 17:13

Status: #baby

Tags: [[2D Game Rendering]]

# Double Buffering

Double buffering renders the next image into a back buffer while the display presents a completed front buffer. When drawing finishes, the buffers exchange roles so the viewer receives a whole frame instead of watching individual drawing operations.

The technique reduces visible flicker and supports synchronization with the [[Vertical Blank Interval]]. It does not by itself prevent [[Screen Tearing]] if the swap occurs while the display is scanning the image.

# References

[[gameprogrammingincplusplus.pdf]]
[[gameprogrammingalgorithmsandtechniques.pdf]]
