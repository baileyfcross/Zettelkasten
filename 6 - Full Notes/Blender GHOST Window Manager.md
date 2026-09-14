2026-09-14 00:20

Status: #baby

Tags: [[Blender GHOST Windowing]]

# Blender GHOST Window Manager

`GHOST_WindowManager` manages the native application windows created at the GHOST layer. Its concern is the collection of operating-system windows wrapped by types such as the X11, Win32, or Cocoa GHOST window classes.

This is narrower than Blender's [[Blender Window Manager Structure]], which organizes application state, screens, events, and operators. GHOST owns the portable native-window abstraction; the higher layer points back to those GHOST windows while adding Blender-specific meaning.

# References

[[coreblenderdevelopment.pdf]]

