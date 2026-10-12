2026-09-29 23:09

Status: #baby

Tags: [[Blender Character Animation Workflow]]

# Foot-Slide Correction

Foot-slide correction synchronizes a planted foot with the character's translation so it remains fixed against the ground during its support phase. A walk action can look convincing in place yet slide visibly when repeated while the rig follows a path at a mismatched speed.

Correction compares stride distance, action duration, NLA repetition, and path timing, then adjusts those values until the contact point stays stable. A ground grid or a deliberately placed 3D cursor provides a spatial reference for the heel across successive frames.

# References

[[learningblender3e.pdf]]
