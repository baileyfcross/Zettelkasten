2026-10-12 23:13

Status: #baby

Tags: [[Unreal Engine VR Development]]

# Physics-Toggled VR Object Pickup

A simple VR pickup attaches a selected actor to the tracked interactor, disables physics while held, and restores physics after detachment. Snapping location and rotation to the controller makes the held pose deterministic, while keeping world scale prevents the pawn hierarchy from resizing the object.

Disabling simulation avoids gravity pulling the object away from the hand, but also makes its transform kinematic. Static-world collision may no longer be resolved as it was during simulation, so the object can pass through geometry. Re-enabling physics on release also detaches a simulated child from its former Blueprint hierarchy; a non-root component may need to be reattached when picked up again.

A more complex alternative keeps physics active, raises damping, disables gravity, and applies a restoring force toward the controller. That retains collision response but requires stable tuning and a policy for large separation. The choice is a tradeoff between predictable attachment and physically constrained contact rather than a purely visual implementation detail.

# References

[[unrealenginevrcookbook.pdf]]

