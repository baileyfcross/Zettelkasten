2026-09-16 00:09

Status: #baby

Tags: [[R Function Design]] · [[R Scripts Functions and Debugging]]

# Explicit Function Return

An explicit function return uses `return()` to stop execution and deliver a value. It is useful for early exits or when several branches should make their result unmistakable.

The returned object should follow a consistent structure across branches so callers do not need to guess its type.

The student companion introduces `return()` as the statement that designates the value produced by a beginner-defined function. Making that output visible in the definition separates the function's reusable result from the local quantities used only to calculate it.

# References

[[essentialsofdatascience.pdf]]

[[rstudentcompanion.pdf]]
