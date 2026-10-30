2026-10-30 15:57

Status: #baby

Tags: [[Java Operators and Pattern Matching]]

# Java Short-Circuit Logical Operators

Java `&&` evaluates its right operand only when the left operand is true, and `||` evaluates the right only when the left is false. This short-circuit behavior permits a guard to establish safety for a later expression, such as checking a reference before dereferencing it.

The unary `!` negates a boolean. Single `&` and `|` can also combine boolean operands, but they evaluate both sides and additionally serve as bitwise integer operators. Choosing the short-circuit form therefore controls both the result and whether a right-side effect or failure can occur.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
