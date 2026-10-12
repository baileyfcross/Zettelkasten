2026-09-18 17:13

Status: #baby

Tags: [[2D Game Rendering]]

# Sprite Sheet

A sprite sheet packs multiple sprite images or animation frames into one larger texture. Rendering selects a rectangular region of that texture rather than loading a separate image for every pose.

Packing reduces texture changes and keeps related frames together. [[Sprite Animation]] advances the selected region according to its own timing rather than assuming one animation image per rendered frame.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]
