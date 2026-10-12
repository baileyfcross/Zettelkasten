2026-10-02 18:09

Status: #baby

Tags: [[Blender Particle and Physics Simulation]]

# Blender Rigid Body Constraints

Blender rigid body constraints connect two physics-enabled objects through a joint represented by an Empty. The Empty supplies the anchor location and axes, while the selected constraint type determines the permitted relationship: fixed, point, hinge, slider, piston, generic, generic spring, or motor.

Linear and angular limits restrict motion, motors specify target velocity and maximum impulse, and a breakable threshold allows a joint to fail under sufficient force. Disabling collision lets constrained bodies overlap without colliding. Because anchor frames are established at the beginning of the animation and remain local to the bodies, initial placement is part of the physical definition of the joint.

# References

[[modelingandanimationusingblender.pdf]]
