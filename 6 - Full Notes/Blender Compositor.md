2026-09-07 23:25

Status: #baby

Tags: [[Blender Video Editing and Compositing]]

# Blender Compositor

Blender's Compositor mixes and processes images through a node network. It can perform simple color and glow adjustments or combine separately rendered and recorded elements into one shot.

The Compositing workspace begins with a Render Layers input connected to a Composite output after Use Nodes is enabled. Additional nodes between them define the image-processing path from source data to final render.

A useful mental model separates input nodes, processing or mixing nodes, and output nodes in a left-to-right flow. For live-action integration, a Movie Clip and transparent Render Layers image can enter an Alpha Over node before reaching Composite, with color correction or other effects inserted along either branch.

# References

[[blenderfordummies4thedition.pdf]]

[[introductiontoblender30.pdf]]
[[learningblender3e.pdf]]
