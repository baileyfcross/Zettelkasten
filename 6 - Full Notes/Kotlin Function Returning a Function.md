2026-10-31 13:27

Status: #baby

Tags: [[Kotlin Functions Null Safety and Delegation]]

# Kotlin Function Returning a Function

A Kotlin function can return a value whose type is itself a function. The outer function chooses or constructs behavior, and the caller can retain and invoke that returned behavior with the declared input and output types.

The returned function may capture values available when it was created, allowing configuration to be separated from later execution. This makes behavior composable while keeping the compiler aware of the complete callable contract.

# References

[[masteringkotlinforjavadevelopers.epub]]
