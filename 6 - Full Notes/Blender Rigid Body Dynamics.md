2026-09-07 23:25

Status: #baby

Tags: [[Blender Simulation and Grease Pencil]] [[Blender Particle and Physics Simulation]]

# Blender Rigid Body Dynamics

Rigid body dynamics simulate objects that move and collide while retaining their form. An active rigid body responds to the calculation, while a passive body participates as an unmoving collider such as a floor.

This is more efficient and appropriate than making a soft body artificially stiff. Initial position and rotation give the solver the starting conditions from which falling, impact, and bouncing develop.

Gress applies the same rigid-body idea to destruction: a model must first be fractured into pieces, then a collider and force can drive their motion. The result still needs suitable fragment shapes, timing, surfacing, and motion blur to read as a real collapse. See [[Rigid Body Fracture and Collision]].

Blender integrates rigid bodies with ordinary animation, parenting, constraints, and drivers. Active bodies can be dynamic or animated, while collision shape, source geometry, mass, friction, bounciness, margin, and collision collections define solver behavior. Separate rigid-body constraints join two bodies through fixed, hinge, slider, piston, spring, generic, or motor relationships.

The source contrasts passive floor and ramp objects with active cubes and a sphere. Giving the sphere an appropriate collision shape and increasing its mass changes the impact from a small nudge to a demolished stack, illustrating that participation type, collision representation, and mass each affect the solve.

# References

[[blenderfordummies4thedition.pdf]]
[[digitalvisualeffectsandcompositing.pdf]]
[[modelingandanimationusingblender.pdf]]

[[testdriveblender.pdf]]
