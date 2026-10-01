2026-10-01 00:39

Status: #baby

Tags: [[OpenGL Rendering Pipeline]]

# OpenGL Coordinate System Setup

An OpenGL drawing can establish a two-dimensional world coordinate system by selecting the projection matrix, loading the identity, and defining an orthographic window with gluOrtho2D. The numeric world bounds need not equal the display's pixel dimensions.

glViewport then identifies the screen rectangle that receives the mapped image. Together the world window and viewport implement a [[Window-to-Viewport Transformation]], automatically scaling and shifting submitted vertices and clipping geometry outside the chosen window. Matching aspect ratios prevents unintended stretching.

# References

[[mathematicsforcomputergraphicsandgameprogramming.pdf]]
