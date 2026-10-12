2026-09-07 23:25

Status: #baby

Tags: [[Blender Video Editing and Compositing]]

# Blender Compositor Backdrop

The Compositor backdrop displays the output connected to an active Viewer node behind the node graph. It makes the image result visible while the network is adjusted.

A Viewer can be added explicitly or created and connected through a shortcut. Sending different node outputs to it turns the backdrop into a diagnostic view of intermediate steps without changing the final Composite output.

This distinction is important when combining footage and a character render: the Alpha Over result can be inspected in the Viewer while only the branch connected to Composite defines the saved frame. The backdrop therefore supports iteration without becoming an implicit output destination.

# References

[[blenderfordummies4thedition.pdf]]
[[learningblender3e.pdf]]
