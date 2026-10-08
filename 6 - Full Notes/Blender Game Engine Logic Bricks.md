2026-10-02 18:09

Status: #baby

Tags: [[Open-Source Game Engine Asset Pipelines]]

# Blender Game Engine Logic Bricks

The historical Blender Game Engine used graphical logic bricks to define event-driven behavior without requiring every interaction to be written in code. These specialized components connected conditions and actions through a visual editor, while Python bindings extended the system when the built-in abstractions were insufficient.

The engine ran a real-time game loop that processed logic, sound, physics, and rendering repeatedly, unlike Blender's ordinary offline rendering path. Its integration allowed the same scene to become an interactive application or simulation. Blender 2.80 removed this engine, making projects dependent on alternatives such as [[UPBGE]] or [[Armory3D Blender-Integrated Game Development]].

The source defines the visual chain explicitly: a Sensor receives keyboard, mouse, or object input; a Controller decides how the signal is relayed; and an Actuator performs motion or another action. Connecting a keyboard sensor through an AND controller to a motion actuator makes the selected actor move along its local axes while the key is pressed.

# References

[[modelingandanimationusingblender.pdf]]

[[testdriveblender.pdf]]
