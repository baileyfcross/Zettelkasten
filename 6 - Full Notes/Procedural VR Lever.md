2026-10-12 23:13

Status: #baby

Tags: [[Unreal Engine VR Development]]

# Procedural VR Lever

A procedural VR lever converts the current interactor position into a constrained local rotation. The lever transforms the tracked hand from world space into the actor's frame, rotates the coordinate basis so it matches the lever axis, and uses the two-argument arc tangent to recover pitch from the local horizontal and vertical components.

Clamping the angle between minimum and maximum pitch produces a stable one-degree-of-freedom control even when the user's hand moves freely in three dimensions. Only the interactor that began the drag may continue or end it, preventing a second hand from unexpectedly taking ownership.

When the angle reaches an activation threshold, an event dispatcher announces that the lever was pulled. A timeline can then interpolate from the current rotation to the stored rest rotation along the shortest rotational path. As with a [[Procedural VR Push Button|procedural button]], the actor exposes a mechanical event while remaining independent of the gameplay consequence bound to it.

# References

[[unrealenginevrcookbook.pdf]]

