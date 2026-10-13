2026-10-12 23:13

Status: #baby

Tags: [[Unreal Engine VR Development]]

# Procedural VR Push Button

A procedural VR push button derives travel from the motion of an overlapping controller or held object instead of relying on an unconstrained physics joint. When overlap begins, the button records the contacting component and its initial world position. Each frame it converts both the initial and current points into the button's local frame and measures displacement along the press axis.

Clamping that displacement between zero and the maximum travel prevents sideways motion or overshoot from breaking the control. When contact ends, interpolation returns the button to its rest position. A threshold comparison and one-shot gate emit the press event only once until the button rises below the activation threshold again.

Local-space calculation lets the complete control be rotated in the level without rewriting its movement logic. An event dispatcher lets level logic bind to the press while keeping the mechanical actor unaware of the door, sequence, or machine it controls. The technique favors controllability over literal physical simulation, which is often desirable when tracked hands can move in ways a real mechanism cannot.

# References

[[unrealenginevrcookbook.pdf]]

