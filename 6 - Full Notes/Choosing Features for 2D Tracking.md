2026-09-15 18:17

Status: #baby

Tags: [[Rotoscopy and Motion Tracking]]

# Choosing Features for 2D Tracking

A reliable track needs a feature that is distinct, contrasted, and visible through the frames being solved. A repeated texture can be confused with another copy of itself; a long straight edge does not uniquely fix movement along that edge; an occluded feature cannot provide continuous evidence. The tracker should preferably be near the depth of the element being attached so parallax does not make the match slide. Choosing the feature well often matters more than enlarging the search region. See [[Tracker Search Window Tuning]].

# References

[[digitalvisualeffectsandcompositing.pdf]]
