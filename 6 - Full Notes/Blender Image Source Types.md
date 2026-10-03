2026-10-02 18:09

Status: #baby

Tags: [[Blender Image and Shader Editing]]

# Blender Image Source Types

Blender image datablocks can represent a single image, an image sequence, a movie, or a generated image. A single image reads one file, while sequences and movies add timing controls such as frame count, start, offset, cycling, refresh, and deinterlacing. Generated images create an in-memory blank or calibration pattern at a chosen size.

The source type determines both the data Blender expects and the controls the [[Blender Image Editor]] exposes. Choosing the correct type prevents a timed asset from being treated as a still and distinguishes a new paintable canvas from a file on disk. Packing embeds the image in the blend file; reloading refreshes an external source.

# References

[[modelingandanimationusingblender.pdf]]
