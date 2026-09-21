2026-09-18 17:13

Status: #baby

Tags: [[Game Loop and Object Architecture]]

# Game Time Factor

A game time factor scales [[Real Delta Time]] before it advances the simulated world. A factor of one makes game time match real time, zero pauses simulation, and other values create slow motion or accelerated play.

The factor changes the time received by game-world updates without requiring the main [[Game Loop]] to stop. Interface animation or other systems that must continue during a pause can remain tied to real time instead.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]
