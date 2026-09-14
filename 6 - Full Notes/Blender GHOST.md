2026-09-14 00:20

Status: #baby

Tags: [[Blender GHOST Windowing]]

# Blender GHOST

GHOST, the Generic Handy Operating System Toolkit, is Blender's internally maintained platform layer. It supplies windows, timers, cursors, clipboard and path services, input state, operating-system events, display settings, and the rendering contexts needed by the application.

Core Blender calls the portable [[Blender GHOST C API]] rather than X11, Win32, or Cocoa directly. GHOST then selects a [[Blender GHOST Platform Class]] and wraps native details, allowing the [[Blender Main Event Loop]] and Blender window manager to remain largely independent of the host operating system.

# References

[[coreblenderdevelopment.pdf]]

