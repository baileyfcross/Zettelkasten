2026-09-28 23:03

Status: #baby

Tags: [[Game Balance and Progression]]

# Viable Balance Range

A viable balance range is the interval between a known value that is too low and one that is too high for a tunable game parameter. With those bounds and reliable higher-or-lower feedback from testing, a designer can use [[Binary Search]] to converge quickly on an appropriate value.

When the bounds are unknown, repeated doubling or halving can discover them. Begin with a provisional value, move exponentially in the indicated direction until the test crosses from insufficient to excessive, and then search within the newly bracketed interval. The method requires observable feedback, not an accurate first guess.

# References

[[introductiontogamesystemdesign.pdf]]
