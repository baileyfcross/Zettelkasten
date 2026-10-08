2026-10-08 00:54

Status: #baby

Tags: [[Open-Source Game Engine Asset Pipelines]]

# Blender Game Engine Actor Physics Types

In the historical Blender Game Engine, an object's physics type determined how it participated in the real-time world. A Static object stayed fixed and did not respond to gravity, while a Dynamic actor could fall, collide, and be moved by game logic.

Motion actuators used the actor's local axes, so forward movement continued to follow the actor after it turned rather than remaining tied to the scene's global axis. Floors and scenery could remain static while the controlled actor and movable obstacles were dynamic. Blender 2.80 removed this engine, but [[UPBGE]] preserves a related workflow.

# References

[[testdriveblender.pdf]]
