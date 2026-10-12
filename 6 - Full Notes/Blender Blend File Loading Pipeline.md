2026-09-14 00:20

Status: #baby

Tags: [[Blender DNA and File Loading]]

# Blender Blend File Loading Pipeline

Factory loading starts at the [[Blender Core Entry Point]], reaches `WM_init()`, and then follows `wm_homefile_read()`, `BKE_blendfile_read_from_memory()`, and `BLO_read_from_memory()`. The loader first creates a [[Blender FileData Structure]], validates the header and DNA, and then parses blocks through a common internal path.

That shared path produces a [[Blender BlendFileData Structure]] whether bytes came from memory or storage. [[Blender LibBlock Linking]] assembles its records into a [[Blender Main Database]], after which [[Blender Context Main Assignment]] makes the new state active.

# References

[[coreblenderdevelopment.pdf]]

