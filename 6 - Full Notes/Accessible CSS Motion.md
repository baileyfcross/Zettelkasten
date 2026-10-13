2026-09-14 01:58

Status: #baby

Tags: [[CSS Transforms Transitions and Animation]]

# Accessible CSS Motion

CSS motion can create accessibility risks when flashing patterns may trigger seizures or large movement produces vestibular discomfort. The source emphasizes avoiding rapid flashing in hazardous ranges and considering how rotations, scaling, and sweeping movement affect sensitive readers.

Animations also share the interface thread with other browser work, so excessive activity can impair responsiveness. Motion should remain a nonessential enhancement whose duration, repetition, and intensity are chosen deliberately.

For SVG and other rich graphics, accessibility also requires control. The source recommends warning users before extreme effects, providing a way to pause or bypass animation, and adapting defaults when reduced motion is requested. A static fallback should preserve the interface's meaning and function, so removing motion never removes the only explanation of a state change.

# References

[[css_thedefinitiveguide.pdf]]
[[usingsvgwithcss3andhtml5.pdf]]
