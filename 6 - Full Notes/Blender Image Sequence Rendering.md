2026-09-07 23:25

Status: #baby

Tags: [[Blender Lighting and Rendering]]

# Blender Image Sequence Rendering

An animation can be rendered as one still image per frame. The output path should point to a dedicated folder because even a short sequence can produce hundreds of files.

Image sequences separate the costly 3D render from later editing and compositing. Individual failed frames can be replaced without rerendering the whole animation, and the sequence can be assembled into video only after the images are complete.

The output format, resolution, frame range, and destination must be set before rendering an animation because each completed frame is written and then removed from temporary memory. Lossless image files preserve an interruption-safe master sequence that can later be loaded into the Video Sequencer or Compositor and encoded as video.

# References

[[blenderfordummies4thedition.pdf]]
[[learningblender3e.pdf]]
