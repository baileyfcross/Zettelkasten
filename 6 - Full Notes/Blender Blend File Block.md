2026-09-14 00:20

Status: #baby

Tags: [[Blender DNA and File Loading]]

# Blender Blend File Block

A blend-file block packages a header with serialized bytes belonging to a particular Blender structure or special record. Header codes distinguish ordinary ID data from global state, user preferences, DNA metadata, termination, and other cases handled by the loader.

For an ordinary library block, the loader reads the serialized structure, converts it to the running version, restores its direct data, and links the result into the [[Blender Main Database]]. The [[Blender LibBlock Linking]] stage turns isolated blocks back into connected application objects.

# References

[[coreblenderdevelopment.pdf]]

