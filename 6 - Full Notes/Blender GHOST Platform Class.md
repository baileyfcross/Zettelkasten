2026-09-14 00:20

Status: #baby

Tags: [[Blender GHOST Windowing]]

# Blender GHOST Platform Class

A GHOST platform class implements abstract system or window operations for one native environment. Examples in the source include system and window classes specialized for Win32, X11, and Cocoa, all sharing interfaces defined by the platform-neutral GHOST layer.

Runtime dispatch selects the concrete implementation after a client enters through the [[Blender GHOST System Interface]] or [[Blender GHOST C API]]. A portable [[Blender GHOST Window Creation]] call therefore ends in the correct native constructor and operating-system API without platform conditionals in the client.

# References

[[coreblenderdevelopment.pdf]]

