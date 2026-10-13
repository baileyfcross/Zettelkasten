2026-09-18 17:13

Status: #baby

Tags: [[Game Physics and Collision]]

# Ray Casting

Ray casting tests a half-line defined by an origin and direction against collision geometry. The result can identify whether an intersection occurs and the parameter or point at which the first hit is found.

Games use ray casts for visibility, weapon traces, camera obstruction, audio obstruction, and [[Object Picking]]. The direction should be normalized when distance is meant to correspond directly to the ray parameter.

Unreal Engine calls ray casts traces and distinguishes searches by object type from searches along a trace channel. A VR gaze trace begins at the tracked camera position and ends at that position plus the normalized camera-forward vector multiplied by the desired distance. Line traces are inexpensive and precise, while sphere, box, or capsule traces trade additional work for a wider acquisition region. A modular interactor can preserve the current hit and issue enter, move, leave, press, and release messages without knowing how the hit object implements them.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]
[[unrealenginevrcookbook.pdf]]
