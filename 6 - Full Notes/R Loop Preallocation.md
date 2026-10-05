2026-10-04 22:56

Status: #baby

Tags: [[R Iteration Logic and Control Flow]]

# R Loop Preallocation

R loop preallocation creates the complete result vector or matrix before iteration and then assigns each computed value into its intended position. This avoids repeatedly growing the object and makes the expected output size and type explicit.

Initial values can also seed a recurrence, as when the first two elements of a Fibonacci vector are defined before the loop calculates later terms. The allocated length must agree with the largest index the loop will write.

# References

[[rstudentcompanion.pdf]]
