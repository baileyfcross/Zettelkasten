2026-09-27 11:46

Status: #baby

Tags: [[Test-Driven Development and Unit Test Design]]

# Red Green Refactor

Red-green-refactor is the repeating test-driven development cycle. Red introduces a focused failing test for missing behavior, green adds the smallest implementation that makes the suite pass, and refactor improves the structure without changing verified behavior.

The order matters because observing the initial failure shows that the test can detect the absence of the behavior. Refactoring while tests remain green separates design improvement from adding another capability.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]
