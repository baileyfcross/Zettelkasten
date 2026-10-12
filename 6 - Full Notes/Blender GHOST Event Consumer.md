2026-09-14 00:20

Status: #baby

Tags: [[Blender GHOST Windowing]]

# Blender GHOST Event Consumer

A GHOST event consumer pairs a callback function with optional client data so GHOST can deliver operating-system events to an application. Blender registers its callback during window-manager initialization and passes the current [[Blender bContext Structure]] as the user-data pointer.

When the [[Blender GHOST Event Pump]] dispatches an event, the consumer invokes that callback. Blender then performs [[Blender GHOST Event Translation]], using the retained context to locate the active window manager and send the translated event toward the correct application window.

# References

[[coreblenderdevelopment.pdf]]

