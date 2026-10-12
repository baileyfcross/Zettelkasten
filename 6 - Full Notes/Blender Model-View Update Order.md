2026-09-14 00:20

Status: #baby

Tags: [[Blender Core Source Architecture]]

# Blender Model-View Update Order

Blender's main loop updates application data before it redraws the interface. Events and operator callbacks first change the model; notifiers record consequences; only after those steps does the draw update refresh what the user sees.

This sequence reflects a model-view-controller organization and prevents the view from presenting an intermediate state. The ordering joins the [[Blender Main Event Loop]] to both the [[Blender Event Distribution Pipeline]] and the [[Blender Editor Draw Pipeline]].

# References

[[coreblenderdevelopment.pdf]]

