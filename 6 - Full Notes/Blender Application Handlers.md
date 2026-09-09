2026-09-08 09:04

Status: #baby

Tags: [[Blender Viewport Drawing API]]

# Blender Application Handlers

Blender application handlers are functions registered to run around recurring events such as frame changes, scene updates, rendering, loading, or saving. They are stored in event-specific lists, so ordinary list operations can add, remove, clear, or inspect the callbacks.

A handler receives the argument shape expected by its event and is passed as a function rather than called during registration. This makes Blender invoke it later whenever the event occurs. Because behavior and timing differed among handlers in the version described by the source, each chosen event should be tested against the task it is meant to support.

# References

[[blenderpythonapi.pdf]]
