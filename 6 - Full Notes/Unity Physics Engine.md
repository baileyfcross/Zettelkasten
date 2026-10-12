2026-10-12 01:03

Status: #baby

Tags: [[Unity Physics and Gameplay Interaction]]

# Unity Physics Engine

Unity integrates separate physics systems for three-dimensional and two-dimensional simulation. Three-dimensional Rigidbody and Collider components use PhysX, while the corresponding 2D components use Box2D.

The families share concepts but are not interchangeable interaction sets. An object should use components from the dimensional system appropriate to its game and neighbors. Physics supplies gravity, forces, contact detection, and constraint solving, while gameplay scripts decide what those simulated events mean.

# References

[[unitygamedevelopmentin24hourssamsteachyourself4e.pdf]]

