2026-09-15 18:17

Status: #baby

Tags: [[Compositing and Keying]]

# Layer-Based and Node-Based Compositing

Layer-based compositing places image elements along a common timeline, making their duration and synchronization immediately visible. Node-based compositing expresses how image operations feed one another, which can make a complex image-processing dependency easier to inspect and reuse. Neither representation changes the fundamental need to manage mattes, color, and the order of operations. A multi-pass shot may benefit from a node network because each rendered component can remain adjustable after the CG render. See [[Multi-Pass Render Compositing]].

# References

[[digitalvisualeffectsandcompositing.pdf]]
