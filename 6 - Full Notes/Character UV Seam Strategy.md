2026-09-29 23:09

Status: #baby

Tags: [[Blender Character Surface Development]]

# Character UV Seam Strategy

A character UV seam strategy cuts the surface into islands that flatten with acceptable distortion while hiding texture discontinuities from important views. Seams can follow less visible sides, clothing boundaries, hairlines, the interior of the lips, or surfaces that will remain under an accessory.

Fewer seams do not automatically produce a better result. An island that is forced to stay connected may stretch badly, while many poorly placed cuts complicate painting. The useful arrangement balances visibility, distortion, paint continuity, and the pixel area required by each feature.

# References

[[learningblender3e.pdf]]
