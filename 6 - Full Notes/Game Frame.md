2026-09-18 17:13

Status: #baby

Tags: [[Game Loop and Object Architecture]]

# Game Frame

A game frame is one complete iteration of the [[Game Loop]], including input processing, world updates, and output generation. The amount of real time between consecutive frames is the [[Real Delta Time]].

Rendering speed determines how often frames are presented, but simulation behavior should not silently depend on that frequency. Frame-based work therefore uses elapsed time when computing motion and other continuous change.

# References

[[gameprogrammingincplusplus.pdf]]
[[gameprogrammingalgorithmsandtechniques.pdf]]
