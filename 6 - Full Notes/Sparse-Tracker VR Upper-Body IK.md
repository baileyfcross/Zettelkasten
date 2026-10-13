2026-10-12 23:13

Status: #baby

Tags: [[Unreal Engine VR Development]]

# Sparse-Tracker VR Upper-Body IK

Sparse-tracker upper-body inverse kinematics estimates an avatar pose from the headset and two motion controllers. The headset supplies a head position and rotation; a multi-bone [[FABRIK Inverse Kinematics|FABRIK]] chain bends the spine toward it. Two-bone solvers place the hands at controller-derived targets, while explicit bone rotations align the avatar's head and hands with the tracked devices.

Controller origins rarely coincide with skeletal hand bones. Sockets placed at the intended grip points provide an offset: the animation system subtracts the bone-to-socket displacement from the controller position before solving the arm. Joint targets bias the elbows toward useful bending planes because a three-dimensional two-bone chain otherwise has infinitely many solutions around its endpoint axis.

The result reproduces tracked upper-body movement without full [[Body Tracking]], but it is an estimate. An untracked torso or legs can make leaning indistinguishable from bending, and the book's head setup assumes the player does not walk away from the expected body location. Sparse IK should therefore be treated as a constrained reconstruction, not measured full-body motion.

# References

[[unrealenginevrcookbook.pdf]]

