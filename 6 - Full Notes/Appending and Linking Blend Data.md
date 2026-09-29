2026-09-28 20:13

Status: #baby

Tags: [[Blender Scene Recovery and Configuration]]

# Appending and Linking Blend Data

Appending copies selected datablocks from another `.blend` file into the current project, after which the copy can diverge independently. Linking instead keeps the imported data dependent on its source library and normally read-only in the receiving file.

The choice is therefore about ownership. Append when the current project should control its own copy; link when a maintained source asset should propagate updates into several projects.

# References

[[howtocheatinblender27x.pdf]]
