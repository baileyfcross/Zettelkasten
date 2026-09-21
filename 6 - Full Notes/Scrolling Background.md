2026-09-18 17:13

Status: #baby

Tags: [[2D Game Rendering]]

# Scrolling Background

A scrolling background presents a game world larger than the display by moving the visible region as the player travels. Single-direction scrolling can recycle background segments after they leave the view, while bidirectional movement must retain or regenerate segments that may reappear.

The camera should begin moving only when the controlled object reaches the intended screen threshold. Separating world position from screen position keeps the world coherent while the viewport changes.

# References

[[gameprogrammingincplusplus.pdf]]
[[gameprogrammingalgorithmsandtechniques.pdf]]
