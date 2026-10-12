2026-09-14 01:18

Status: #baby

Tags: [[Open-Source Game Engine Asset Pipelines]]

# Godot Project Folder as Asset Source

Godot treats its project folder as the source of files shown in the editor's FileSystem panel. Copying a supported asset into that folder triggers import and makes the resulting resource available to the project.

The relationship is bidirectional at the file level: changes made in the folder appear in the panel, and organization in the project corresponds to stored files. Asset naming and dependency placement therefore belong to the pipeline rather than being an afterthought inside the editor.

# References

[[creatinggameenvironmentsinblender3d.pdf]]

