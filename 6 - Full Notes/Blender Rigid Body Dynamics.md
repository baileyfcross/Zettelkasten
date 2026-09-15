2026-09-07 23:25

Status: #baby

Tags: [[Blender Simulation and Grease Pencil]]

# Blender Rigid Body Dynamics

Rigid body dynamics simulate objects that move and collide while retaining their form. An active rigid body responds to the calculation, while a passive body participates as an unmoving collider such as a floor.

This is more efficient and appropriate than making a soft body artificially stiff. Initial position and rotation give the solver the starting conditions from which falling, impact, and bouncing develop.

Gress applies the same rigid-body idea to destruction: a model must first be fractured into pieces, then a collider and force can drive their motion. The result still needs suitable fragment shapes, timing, surfacing, and motion blur to read as a real collapse. See [[Rigid Body Fracture and Collision]].

# References

[[blenderfordummies4thedition.pdf]]
[[digitalvisualeffectsandcompositing.pdf]]
