2026-09-08 09:04

Status: #baby

Tags: [[Blender Viewport Drawing API]]

# Button-Activated Viewport Drawing

A Blender operator can toggle a viewport draw handler in response to a panel button. When the overlay is inactive, execution adds the handler and stores its reference; when active, execution removes it and clears the reference. A window-level Boolean can keep the panel's displayed state consistent with the actual handler.

This lifecycle solves a problem with one-off scripts: a persistent draw callback may otherwise remain attached until Blender restarts. The button gives the user control, while unregistration provides a final cleanup path if the add-on is disabled during drawing.

# References

[[blenderpythonapi.pdf]]
