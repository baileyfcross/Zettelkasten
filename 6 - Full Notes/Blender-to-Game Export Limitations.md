2026-09-28 20:13

Status: #baby

Tags: [[Blender Game Asset Export]]

# Blender-to-Game Export Limitations

Game export carries a portable subset of a Blender scene rather than the complete application state. Scene ambience, fog, native materials, raw constraints, modifier parameters, and simulation systems commonly fail to transfer as functional equivalents.

Transfer therefore depends on conversion: modifiers become mesh results, procedural motion becomes keyframes, and textures travel as files from which engine materials are rebuilt. A small representative export test should verify each required feature before the project commits to a pipeline.

# References

[[howtocheatinblender27x.pdf]]
