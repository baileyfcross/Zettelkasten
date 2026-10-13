2026-10-12 23:13

Status: #baby

Tags: [[Unreal Engine VR Development]]

# FABRIK Inverse Kinematics

Forward and Backward Reaching Inverse Kinematics solves a joint chain by iteratively repositioning its joints rather than deriving one closed-form set of angles. The backward pass moves the end bone to the target and walks toward the root while preserving each segment's length. Because that displaces the root, the forward pass restores the root and walks back toward the tip.

Repeating the two passes converges toward an endpoint goal and allows a chain with more than two bones. The iteration limit trades cost against accuracy. This makes FABRIK useful for a spine or another multi-joint chain, while an analytic two-bone solver is simpler for an arm or leg whose root, middle joint, and endpoint are known.

An endpoint alone does not fully determine a three-dimensional pose. A joint target or other directional preference is still needed where the chain has multiple valid bending configurations. In Unreal's animation graph, coordinate-space choices for the goal must also match the tracked transform supplied by the pawn.

# References

[[unrealenginevrcookbook.pdf]]

