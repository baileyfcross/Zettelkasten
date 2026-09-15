2026-09-15 18:17

Status: #baby

Tags: [[Rotoscopy and Motion Tracking]]

# Tracking Pattern Search and Anchor Regions

A two-dimensional tracker separates three jobs: a pattern region describes the image feature to recognize, a search region bounds where to look for it in the next frame, and an anchor locates the point whose motion will be applied. A good pattern has enough stable, distinct texture to be found repeatedly. An anchor can be placed at the desired attachment point even when the recognizable feature is nearby rather than exactly on that point. Search size must be tuned, as described in [[Tracker Search Window Tuning]].

# References

[[digitalvisualeffectsandcompositing.pdf]]
