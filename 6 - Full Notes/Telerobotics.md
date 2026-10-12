2026-09-05 13:11

Status: #baby

Tags: [[XR Environments]] [[Prosthetic and Robotic Haptic Systems]] [[XR Training and Professional Practice]] [[Human-Robot Interaction and Augmentation]]

# Telerobotics

Telerobotics is the remote operation of a robot that is geographically separated from its user. Because robots act in the physical world and can have many [[Degrees of Freedom]], their control often benefits from a [[3D User Interface]].

The interface must map the user's input to remote movement and return sufficient feedback for safe, accurate control. [[Latency]], incomplete sensory information, and mismatches between the user's controls and the robot's capabilities can make the task harder.

Force-reflecting master devices can close the loop by returning loads measured at the remote mechanism to the operator's hand. This lets human perception, planning, and error correction guide a robot working in a hazardous, underwater, medical, or otherwise inaccessible environment. The mapping must remain stable and timely; delayed or distorted forces can misrepresent contact and destabilize control.

Immersive viewing can couple the operator's head motion to a remote camera or robot viewpoint, producing [[Telepresence]] while leaving physical action to the machine. Space, undersea, terrestrial, airborne, and medical operations illustrate the same constraint: communication delay and limited feedback determine which motions can be directly teleoperated and which require local autonomy.

Remote embodiment also multiplies human presence: the operator can observe and act in a dangerous, distant, or inaccessible place without moving their body there. The complete system includes the robot, network, interface, operator, local environment, and any nearby people. Safe design must specify what the robot does when the link degrades and how authority transfers between direct control and local autonomy.

# References

[[3duserinterfaces2ande.pdf]]
[[haptics.epub]]
[[practicalaugmentedreality.pdf]]

[[robots.epub]]
