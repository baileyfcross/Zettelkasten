2026-10-01 00:39

Status: #baby

Tags: [[OpenGL Rendering Pipeline]]

# OpenGL Matrix Transformations

OpenGL transforms submitted points through a current transformation matrix. Changing that matrix scales, rotates, translates, or projects every subsequent vertex without requiring the application to rewrite the object's stored coordinates.

Object transformation and coordinate transformation offer two interpretations of the same machinery: one moves points within a fixed frame, while the other re-expresses unchanged points in a new frame. Because transformation calls modify or compose the current matrix, call order controls the result. Loading an identity matrix establishes a known baseline before building a new view or object transform.

# References

[[mathematicsforcomputergraphicsandgameprogramming.pdf]]
