2026-09-28 22:14

Status: #baby

Tags: [[Unity Game Development]]

# Unity Component

A Unity component is a focused unit of data and behavior attached to a [[Unity GameObject]]. Components add capabilities such as transform, rendering, collision, physics, audio, or scripted behavior without changing the GameObject's identity.

Component-oriented design favors small, reusable responsibilities over monolithic object classes. An object's runtime behavior emerges from the combination of its components and their interactions. This improves reuse and editor visibility, but it also makes dependencies important: a renderer needs geometry, physics movement normally needs a collider, and scripts must handle missing components deliberately.

# References

[[introductiontogamedesignprototypinganddevelopment3e.pdf]]

