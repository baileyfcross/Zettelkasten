2026-09-14 00:20

Status: #baby

Tags: [[Blender Operator and Event System]]

# Blender Window Event Processing

The first event stage in Blender's main loop asks GHOST to gather and dispatch native events, then checks window timers. If nothing occurred, the process briefly sleeps so the application does not consume the processor continuously while idle.

GHOST callbacks perform [[Blender GHOST Event Translation]] and fill each [[Blender Window Event Queue]]. The next stage invokes the [[Blender Event Distribution Pipeline]], which adds Blender-specific spatial and contextual routing beyond the portable window layer.

# References

[[coreblenderdevelopment.pdf]]

