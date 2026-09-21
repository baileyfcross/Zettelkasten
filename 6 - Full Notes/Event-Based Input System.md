2026-09-18 17:13

Status: #baby

Tags: [[Game Input Systems]]

# Event-Based Input System

An event-based input system converts device-specific changes into named gameplay actions and dispatches them to interested systems. Gameplay code responds to the meaning of an event rather than repeatedly checking particular keys or buttons.

This indirection supports remapping and multiple devices. It also lets different game states subscribe to the actions relevant to them without coupling every object to the hardware interface.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]
