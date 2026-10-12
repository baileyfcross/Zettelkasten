2026-09-14 00:20

Status: #baby

Tags: [[Blender GHOST Windowing]]

# Blender GHOST Event Pump

Blender's window manager pumps GHOST events by calling the process function and, when work is available, the dispatch function. Processing obtains native events; dispatching delivers them to the registered [[Blender GHOST Event Consumer]].

The pump also checks Blender timers and briefly yields when neither native nor timer events are pending. This sequence forms the first stage of the [[Blender Main Event Loop]], before [[Blender Window Event Processing]] translates and routes the resulting work.

# References

[[coreblenderdevelopment.pdf]]

