2026-11-11 18:27

Status: #baby

Tags: [[Test-Driven Development and Unit Test Design]]

# Boundary Value Testing

Boundary value testing selects inputs at, immediately inside, and immediately outside the limits of a valid range. For a permitted range from 0 through 100, cases such as -1, 0, 1, 99, 100, and 101 distinguish correct endpoints from off-by-one comparisons.

Boundaries also include empty and full collections, first and last positions, maximum lengths, zero denominators, and transitions between states. These cases are disproportionately useful because many implementations change control flow exactly where the boundary is crossed.

# References

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]

