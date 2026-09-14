2026-09-14 01:18

Status: #baby

Tags: [[Open-Source Game Engine Asset Pipelines]]

# Armory3D Cycles Material Compilation

Armory3D uses Cycles-style material nodes as an authoring representation and precompiles supported networks into shaders for real-time rendering. The same Blender scene can therefore remain inspectable through Cycles while targeting an interactive pipeline.

Cycles compatibility is a source-language relationship, not proof that every offline effect has a real-time equivalent. Materials, lighting, and baked data should be tested in the Armory runtime, especially when a node network relies on expensive or unsupported behavior.

# References

[[creatinggameenvironmentsinblender3d.pdf]]

