2026-10-30 15:57

Status: #baby

Tags: [[Java Operators and Pattern Matching]]

# Java Reference and Value Equality

For primitive operands, Java `==` compares represented values after applicable numeric promotion. For reference operands, it compares identity: both values must designate the same object or both be null.

Logical equality for objects is supplied by an `equals` implementation and may compare content or domain identity. The distinction matters for wrappers, strings, records, and collection elements; a reference comparison can succeed because two variables share an object without proving that distinct objects with equivalent content should compare unequal.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
