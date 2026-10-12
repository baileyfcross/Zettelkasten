2026-09-14 00:20

Status: #baby

Tags: [[Blender DNA and File Loading]]

# Blender Factory Startup Data

Blender's factory startup file is embedded into the executable as a byte array. During the build, the `datatoc` tool converts the repository's `startup.blend` into generated C source whose `datatoc_startup_blend` array preserves the original file bytes.

At application initialization, `WM_init()` selects this in-memory source for a factory start and sends it through the ordinary [[Blender Blend File Loading Pipeline]]. Embedding the data lets Blender reconstruct a known [[Blender Main Database]] without depending on an external startup file.

# References

[[coreblenderdevelopment.pdf]]

