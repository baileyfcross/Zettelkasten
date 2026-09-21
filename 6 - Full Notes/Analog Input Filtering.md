2026-09-18 17:13

Status: #baby

Tags: [[Game Input Systems]]

# Analog Input Filtering

Analog input filtering removes small, unintended, or noisy values from an [[Analog Input Device]]. A dead zone can map values near the neutral position to zero, while rescaling preserves useful control across the remaining range.

Filtering prevents drift and unstable motion. The chosen threshold must be large enough to suppress hardware noise without erasing deliberate subtle input.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]
