2026-09-14 00:20

Status: #baby

Tags: [[Blender DNA and File Loading]]

# Blender Context Main Assignment

After a blend file has been read and linked, Blender must replace the current application's database with the newly constructed one. Setup functions carry the `Main` pointer from a [[Blender BlendFileData Structure]] and eventually call the context accessor that installs it in the [[Blender bContext Structure]].

This is the final state-transfer step of the [[Blender Blend File Loading Pipeline]]. It keeps the loader responsible for reconstruction while the [[Blender CTX API]] controls how active application state is assigned and later retrieved by operators, editors, and the main loop.

# References

[[coreblenderdevelopment.pdf]]

