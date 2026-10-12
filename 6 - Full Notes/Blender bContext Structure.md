2026-09-14 00:20

Status: #baby

Tags: [[Blender DNA and File Loading]]

# Blender bContext Structure

`bContext` is the top-level runtime structure used to carry Blender's current application state through operations. One portion holds window-manager context such as the window, workspace, screen, area, region, and active UI store; another holds data context such as the [[Blender Main Database]] and current scene.

Most callers use accessor functions instead of manipulating the structure directly, preserving its encapsulation behind the [[Blender CTX API]]. The same context pointer passes through startup loading, the [[Blender Main Event Loop]], operator callbacks, and editor drawing so each stage can resolve the state relevant to its work.

# References

[[coreblenderdevelopment.pdf]]

