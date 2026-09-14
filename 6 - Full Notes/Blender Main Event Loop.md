2026-09-14 00:20

Status: #baby

Tags: [[Blender Core Source Architecture]]

# Blender Main Event Loop

`WM_main()` is Blender's continuously running application loop. Each pass obtains and dispatches operating-system events, processes the window and editor handlers that respond to them, handles deferred notifiers, and then updates drawing.

The loop passes a [[Blender bContext Structure]] through each high-level stage so the same current application state remains available. Low-level input arrives through the [[Blender GHOST Event Pump]], becomes Blender-specific work in the [[Blender Event Distribution Pipeline]], and ends with the [[Blender Model-View Update Order]].

# References

[[coreblenderdevelopment.pdf]]

