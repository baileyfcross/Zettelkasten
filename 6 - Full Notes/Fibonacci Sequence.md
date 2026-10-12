2026-10-04 22:56

Status: #baby

Tags: [[R Iteration Logic and Control Flow]]

# Fibonacci Sequence

The Fibonacci sequence is defined by two initial values followed by a recurrence in which each term equals the sum of the preceding two. Its computation therefore requires both stored state and an iteration that begins only after the seed positions have been assigned.

In R, a preallocated vector holds the terms and a [[R For Loop|for loop]] assigns `r[i+1]` from `r[i]` and `r[i-1]`. Changing the two seeds generates a different sequence under the same recurrence.

# References

[[rstudentcompanion.pdf]]
