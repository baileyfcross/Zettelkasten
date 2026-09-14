2026-09-14 00:20

Status: #baby

Tags: [[Blender DNA and File Loading]]

# Blender FileData Structure

`FileData` is the loader's low-level representation of an input source and its decoded format information. It stores the reading strategy, file headers, structural metadata, and the state needed to walk serialized blocks even when the bytes originated from memory rather than a disk file.

Memory and file entry functions construct it differently but converge on the same internal parser. That convergence allows the [[Blender Blend File Loading Pipeline]] to produce a common [[Blender BlendFileData Structure]] after validating the [[Blender Blend File Header]] and reading the [[Blender DNA1 Block]].

# References

[[coreblenderdevelopment.pdf]]

