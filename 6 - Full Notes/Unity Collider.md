2026-09-28 22:14

Status: #baby

Tags: [[Unity Game Development]]

# Unity Collider

A Unity Collider gives a GameObject a shape that the physics system can test for contact. Sphere, capsule, and box colliders approximate common volumes efficiently, while a mesh collider can follow detailed geometry at greater computational cost and with additional restrictions.

Collision shape should be only as detailed as gameplay requires. A collider without a [[Unity Rigidbody]] normally behaves as an immovable obstacle, while a moving physical object uses both components so simulation and contact remain synchronized. Fast objects and thin surfaces can still exceed the assumptions of discrete collision checks.

# References

[[introductiontogamedesignprototypinganddevelopment3e.pdf]]

