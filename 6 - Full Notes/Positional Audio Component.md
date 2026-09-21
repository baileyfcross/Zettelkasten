2026-09-20 23:34

Status: #baby

Tags: [[Game Audio Programming]]

# Positional Audio Component

A positional audio component associates a [[Game Actor]] with one or more spatial sound instances. As the actor moves, the component updates the emitter position and orientation supplied to the audio engine.

The component makes spatial playback reusable across actor types and keeps transforms synchronized. It can stop owned events when removed so sounds do not outlive the world object that created them.

# References

[[gameprogrammingincplusplus.pdf]]
