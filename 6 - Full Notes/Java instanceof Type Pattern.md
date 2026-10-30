2026-10-30 15:57

Status: #baby

Tags: [[Java Operators and Pattern Matching]]

# Java instanceof Type Pattern

An `instanceof` type pattern combines a runtime type test with a cast and local binding. When `value instanceof Performer performer` succeeds, the pattern variable has the tested type and is available only where the compiler can prove the match remains true.

This removes a repeated explicit cast and keeps the bound name within a flow-sensitive scope. A failed match, including a null input, does not produce the variable. The pattern refines an existing reference; it does not convert an incompatible object into the requested type.

Flow-sensitive scope also follows Boolean control flow. A binding is available on the right side of `&&` after a successful test, and after an early return from a negated test the compiler can know that the remaining path has the matched type. It is not safely available through an `||` branch where the type test may have failed.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
[[java25andbeyond_modernjavamadeeasy.epub]]
