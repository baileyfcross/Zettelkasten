2026-09-14 00:20

Status: #baby

Tags: [[Blender GHOST Windowing]]

# Blender GHOST Event Manager

The GHOST event manager stores and dispatches low-level events obtained from the operating system. Event subclasses distinguish keys, mouse buttons, cursor motion, drag-and-drop activity, and other native interactions before Blender assigns application-specific semantics.

Clients register a [[Blender GHOST Event Consumer]], then the [[Blender GHOST Event Pump]] gathers and dispatches available work. Blender's callback performs [[Blender GHOST Event Translation]] so native events can enter its own window queues and region handlers.

# References

[[coreblenderdevelopment.pdf]]

