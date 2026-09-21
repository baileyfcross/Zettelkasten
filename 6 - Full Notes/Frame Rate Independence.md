2026-09-18 17:13

Status: #baby

Tags: [[Game Loop and Object Architecture]]

# Frame Rate Independence

Frame rate independence means that a simulated change is based on elapsed time rather than on the number of rendered frames. A moving object's speed is multiplied by delta time, so it covers approximately the same distance per second on fast and slow machines.

Without this relationship, higher frame rates make movement and animation advance more often and therefore run faster. [[Real Delta Time]] decouples continuous gameplay behavior from display frequency.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]
