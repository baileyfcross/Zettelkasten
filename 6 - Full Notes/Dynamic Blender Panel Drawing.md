2026-09-08 09:04

Status: #baby

Tags: [[Blender Viewport Drawing API]]

# Dynamic Blender Panel Drawing

Blender calls a panel's `draw` method repeatedly as the interface updates, so its layout can respond to current state. A viewport-overlay panel can show a play-style action when drawing is disabled and a pause-style action when the handler is active.

Dynamic drawing can also conditionally reveal controls, labels, and icons without permanently rebuilding the panel class. The method should read authoritative scene or window state each time rather than relying on a visual assumption, ensuring that the controls describe what execution will actually do.

# References

[[blenderpythonapi.pdf]]
