2026-09-18 17:13

Status: #baby

Tags: [[Game Loop and Object Architecture]]

# Frame Limiting

Frame limiting prevents a [[Game Loop]] from beginning the next frame until a minimum frame duration has elapsed. It caps the maximum frame rate and can keep the program from consuming all available processing time when work finishes early.

The limiter belongs after input, update, and output work. It should use accurate timing and should not replace [[Frame Rate Independence]], because actual frame durations still vary.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]
