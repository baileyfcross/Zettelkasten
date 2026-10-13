2026-10-04 12:03

Status: #baby

Tags: [[XR Human Factors and Safety]]

# XR Physical Boundary Safety

XR physical boundary safety prevents a user whose attention is captured by a display from colliding with real objects, striking bystanders, or damaging property. The risk is greatest when an opaque [[Head-Worn Display]] blocks the surrounding room while the application asks the user to walk, punch, swing a controller, or reach beyond a cleared area.

A system can warn about a configured play boundary, reveal the physical scene through a front-facing camera, restrict interaction to orientation-only tracking, or use locomotion controls that keep the user in place. These mechanisms depend on accurate [[3D Tracking]] and should fail conservatively when the boundary or camera feed is unavailable.

[[Augmented Reality]] preserves more of the physical view, but overlays can still distract or obscure hazards. Boundary design must account for the user's body and handheld equipment, not merely the headset position, and should protect nearby people who are not represented in the virtual scene.

Locomotion hardware and perceptual redirection can keep virtual travel inside a smaller area. An [[Omnidirectional Treadmill]] supports multi-directional steps while retaining the body near one location, whereas [[Redirected Walking]] gradually bends the physical path without making the virtual route appear curved. Both still require clearance, tracking, and a conservative response when the user approaches a real limit.

# References

[[practicalaugmentedreality.pdf]]
[[virtualreality.epub]]
