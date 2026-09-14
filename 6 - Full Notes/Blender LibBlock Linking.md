2026-09-14 00:20

Status: #baby

Tags: [[Blender DNA and File Loading]]

# Blender LibBlock Linking

LibBlock linking turns converted blend-file records into connected Blender objects. For each ordinary block, `read_libblock()` reads the current-version structure, restores directly owned data through a type-specific `direct_link_*()` routine, and identifies the datablock through its `ID` header.

After direct data is repaired, `lib_link_all()` resolves relationships among datablocks and joins the results into the [[Blender Main Database]]. This staged approach separates [[Blender Blend File Version Conversion]] from pointer restoration and makes both memory-based and file-based loads follow the same logic.

# References

[[coreblenderdevelopment.pdf]]

