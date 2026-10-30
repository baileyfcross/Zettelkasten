2026-10-30 15:57

Status: #baby

Tags: [[Java Operators and Pattern Matching]]

# Java instanceof Type Pattern

An `instanceof` type pattern combines a runtime type test with a cast and local binding. When `value instanceof Performer performer` succeeds, the pattern variable has the tested type and is available only where the compiler can prove the match remains true.

This removes a repeated explicit cast and keeps the bound name within a flow-sensitive scope. A failed match, including a null input, does not produce the variable. The pattern refines an existing reference; it does not convert an incompatible object into the requested type.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
