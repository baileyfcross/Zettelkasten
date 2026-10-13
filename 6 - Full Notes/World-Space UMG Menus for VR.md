2026-10-12 23:13

Status: #baby

Tags: [[Unreal Engine VR Development]]

# World-Space UMG Menus for VR

A world-space UMG menu renders a conventional Unreal Motion Graphics widget onto a three-dimensional surface. This lets the menu receive the same perspective and occlusion cues as nearby geometry, and lets the user turn toward different regions instead of keeping every control fixed at the periphery of a [[Head-Worn Display]].

An orthographically overlaid, head-locked interface can appear to sit at optical infinity while being drawn over nearer objects, creating conflicting depth evidence. Peripheral controls may also become blurred or clipped because headset optics are clearest near the center and users have different eye relief. A world-space widget addresses those problems by giving the interface a physical distance and allowing head movement to inspect it.

The implementation separates the 2D widget, an actor containing a 3D Widget Component, and a pawn containing the input component. Rendering the widget at a higher draw size and scaling its surface down can improve text clarity, although translucency and persistent visibility still carry cost. Diegetic controls should be considered before adding a menu when the state can be conveyed through the virtual object itself.

# References

[[unrealenginevrcookbook.pdf]]

