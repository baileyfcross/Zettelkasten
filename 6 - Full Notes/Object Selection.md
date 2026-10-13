2026-09-05 13:11

Status: #baby

Tags: [[Spatial Interaction]]

# Object Selection

Object selection is the task of acquiring or identifying one object or a subset of objects from the available set. It is also called target acquisition and is a canonical [[3D Manipulation]] task.

Selection difficulty depends on target size and distance, object density, occlusion, number of targets, input precision, and the [[Depth Cue]]s provided by the display. Pointing techniques often perform well for remote selection, while grasping techniques are generally more suitable for subsequent manipulation.

Dense scenes can use [[Progressive Refinement]]: a coarse first action narrows the candidates and a simpler second action identifies the final target.

Gaze selection can supplement a narrow [[Ray Casting|ray cast]] with an intent score. The dot product between the normalized view direction and the direction to a candidate ranks angular alignment, but discards distance; minimizing the corresponding arc length restores a distance penalty. A sphere trace gives a simpler collision-aware acquisition cone. Pure angular ranking also needs an occlusion test, or it may select an object through a wall.

# References

[[3duserinterfaces2ande.pdf]]
[[unrealenginevrcookbook.pdf]]
