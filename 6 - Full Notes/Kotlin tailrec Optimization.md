2026-10-31 13:27

Status: #baby

Tags: [[Kotlin Functions Null Safety and Delegation]]

# Kotlin tailrec Optimization

The `tailrec` modifier asks Kotlin to optimize a recursive function whose recursive call is the final operation on the returning path. In that form, the next iteration does not need the current call's unfinished computation.

Eligible tail recursion can be compiled into repetition that avoids growing the call stack for each step. A recursive call nested inside another calculation is not in tail position, because the current frame must remain available to perform work after that call returns.

# References

[[masteringkotlinforjavadevelopers.epub]]
