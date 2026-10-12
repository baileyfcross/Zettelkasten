2026-09-18 17:13

Status: #baby

Tags: [[3D Game Rendering]]

# Screen Space

Screen space is the two-dimensional coordinate system of the rendered viewport. The graphics pipeline maps projected geometry into pixel positions while retaining depth information for visibility testing.

Screen coordinates are useful for interface alignment and selection, but they no longer directly express the original three-dimensional position. [[Unprojection]] reverses part of the pipeline when a screen point must define a world-space ray.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]
