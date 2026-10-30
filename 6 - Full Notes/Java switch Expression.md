2026-10-30 15:57

Status: #baby

Tags: [[Java Control Flow and Exceptions]]

# Java switch Expression

A Java switch expression selects one branch and yields a value. Arrow labels avoid fall-through, several case constants can share a branch, and `yield` returns a value from a block-shaped branch that needs multiple statements.

Because the result must have a compatible type, the compiler checks that the expression is exhaustive. An enum or sealed hierarchy can supply a closed set of cases; otherwise a default branch commonly covers remaining values. The expression form is useful when every branch computes the same conceptual result.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
