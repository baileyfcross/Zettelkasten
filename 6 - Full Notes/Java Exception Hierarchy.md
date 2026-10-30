2026-10-30 15:57

Status: #baby

Tags: [[Java Control Flow and Exceptions]]

# Java Exception Hierarchy

Java represents abnormal execution with objects rooted at `Throwable`. `Error` describes serious virtual-machine or environmental failures that ordinary application logic generally cannot recover from, while `Exception` contains conditions an application may catch or propagate.

The thrown object's runtime type determines which compatible catch clause handles it. Catching a broad superclass can hide distinctions needed for recovery, so handlers should normally name the most specific useful type and preserve the original cause when translating an exception across a boundary.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
