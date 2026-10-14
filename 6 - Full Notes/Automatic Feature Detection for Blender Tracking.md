2026-09-07 23:25

Status: #baby

Tags: [[Blender Motion Tracking]]

# Automatic Feature Detection for Blender Tracking

Detect Features analyzes the current video frame and places markers on image regions Blender considers trackable. It accelerates initial marker placement but does not guarantee that every proposed feature will remain stable through the shot.

More markers are not automatically better. A modest set of strong tracks can solve a shot while avoiding needless computation, and detected markers still require review, tracking, and cleanup.

Automatic placement is most useful as a source of candidates, not as a substitute for shot knowledge. Features should still be static, distinct across frames, distributed through depth, and present long enough to support a solve; unstable suggestions can be replaced with manually placed markers near the region where CG will touch the plate.

# References

[[blenderfordummies4thedition.pdf]]
[[learningblender3e.pdf]]
