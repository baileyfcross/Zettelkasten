2026-09-18 17:13

Status: #baby

Tags: [[Game Loop and Object Architecture]]

# Real Delta Time

Real delta time is the wall-clock interval between the current [[Game Frame]] and the preceding one. It measures how much actual time elapsed regardless of whether the game is paused, slowed, or accelerated.

Multiplying it by the [[Game Time Factor]] produces the amount of simulation time supplied to updateable objects. Keeping the two values separate lets presentation timing and gameplay timing be controlled independently.

# References

[[gameprogrammingincplusplus.pdf]]
[[gameprogrammingalgorithmsandtechniques.pdf]]
