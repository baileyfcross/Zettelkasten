2026-09-28 20:13

Status: #baby

Tags: [[Blender Scene Recovery and Configuration]]

# Appending and Linking Blend Data

Appending copies selected datablocks from another `.blend` file into the current project, after which the copy can diverge independently. Linking instead keeps the imported data dependent on its source library and normally read-only in the receiving file.

The choice is therefore about ownership. Append when the current project should control its own copy; link when a maintained source asset should propagate updates into several projects.

The source demonstrates appending an Object datablock from a saved aircraft `.blend` file. The File Browser enters the library, exposes its datablock categories, and copies the selected object into the current scene at the 3D cursor, after which it can be scaled, moved, and edited independently.

# References

[[howtocheatinblender27x.pdf]]

[[testdriveblender.pdf]]
