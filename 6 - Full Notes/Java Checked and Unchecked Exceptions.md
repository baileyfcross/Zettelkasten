2026-10-30 15:57

Status: #baby

Tags: [[Java Control Flow and Exceptions]]

# Java Checked and Unchecked Exceptions

A checked Java exception is an `Exception` that is not a `RuntimeException`; the compiler requires a method to catch it or declare it with `throws`. An unchecked exception is a `RuntimeException` subtype and can propagate without a declaration.

Checked exceptions make anticipated external failures visible in signatures, while unchecked exceptions often indicate invalid arguments, state, or programming defects. The category does not decide whether a condition is important. Recovery belongs where the program has enough context to choose a meaningful next action.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
