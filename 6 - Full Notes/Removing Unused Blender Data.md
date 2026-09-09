2026-09-08 09:04

Status: #baby

Tags: [[Automated Blender Texturing and Rendering]]

# Removing Unused Blender Data

Repeated script tests can leave unused materials and textures in Blender's datablocks even after scene objects are deleted. Blender avoids name collisions by adding numeric suffixes, so this accumulation can obscure which resource the current script actually uses.

A cleanup routine inspects each datablock's user count and removes those with no remaining users. The user check protects resources still assigned to objects. Clearing unused data before another test creates a reproducible starting state and prevents old materials from being mistaken for newly generated results.

# References

[[blenderpythonapi.pdf]]
