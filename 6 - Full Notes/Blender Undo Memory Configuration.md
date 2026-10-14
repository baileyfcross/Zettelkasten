2026-09-28 20:13

Status: #baby

Tags: [[Blender Scene Recovery and Configuration]]

# Blender Undo Memory Configuration

Blender's undo history trades recoverability for memory use. Increasing the number of undo steps expands how far an artist can move backward through edits, while an undo memory limit prevents that history from consuming an uncontrolled amount of RAM.

The appropriate setting depends on scene size and available memory. Dense geometry makes each stored state more expensive, so a very deep history can become a performance cost rather than pure protection.

# References

[[howtocheatinblender27x.pdf]]
