2026-10-12 01:03

Status: #baby

Tags: [[Unity 2D Interface and Mobile Development]]

# Unity Sorting Layer

A Unity sorting layer groups sprites and tilemaps into major front-to-back rendering bands. The order of those layers establishes broad depth categories such as background, play space, effects, and foreground.

Within a layer, Order in Layer provides finer priority, with larger values drawn above smaller values. Setting both explicitly on a [[Unity Sprite Renderer]] prevents sprites from disappearing behind unrelated artwork or changing order because of incidental z coordinates.

# References

[[unitygamedevelopmentin24hourssamsteachyourself4e.pdf]]

