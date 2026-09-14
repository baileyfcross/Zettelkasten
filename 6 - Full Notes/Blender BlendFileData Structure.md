2026-09-14 00:20

Status: #baby

Tags: [[Blender DNA and File Loading]]

# Blender BlendFileData Structure

`BlendFileData` is the higher-level result assembled by Blender's loader. It can carry the reconstructed `Main` database, user preferences, flags, filename information, active screen and scene pointers, the current view layer, and the recognized file type.

Unlike the low-level [[Blender FileData Structure]], it represents application-ready state rather than a decoding mechanism. Once [[Blender LibBlock Linking]] has completed, setup functions use this object for [[Blender Context Main Assignment]] and related startup configuration.

# References

[[coreblenderdevelopment.pdf]]

