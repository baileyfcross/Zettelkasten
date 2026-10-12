2026-09-14 01:18

Status: #baby

Tags: [[Open-Source Game Engine Asset Pipelines]]

# Godot Node-Based Scene Structure

Godot scenes are trees of nodes, each supplying a focused capability such as spatial transformation, mesh display, camera behavior, light, interface, or script logic. A root establishes the scene's type and organizes its descendants.

Imported Blender assets must fit that structure through instances and child nodes. Clear hierarchy preserves reusable groups and makes it easier to attach engine behavior without altering the geometry source itself.

# References

[[creatinggameenvironmentsinblender3d.pdf]]

