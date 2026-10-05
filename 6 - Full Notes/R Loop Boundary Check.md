2026-10-04 22:56

Status: #baby

Tags: [[R Iteration Logic and Control Flow]]

# R Loop Boundary Check

An R loop boundary check evaluates the first few and last few iterations by hand to verify index values, required predecessors, and target positions. Boundary reasoning catches off-by-one errors that may leave an initial value unused, request position zero, or write beyond a preallocated object.

The book checks a Fibonacci recurrence by substituting the early index values into the assignment before trusting a longer run. The same technique applies to nested loops, where both row and column limits must be verified.

# References

[[rstudentcompanion.pdf]]
