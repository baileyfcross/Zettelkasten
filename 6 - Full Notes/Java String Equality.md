2026-10-30 15:57

Status: #baby

Tags: [[Java Values Strings and Core Types]] · [[Java String Processing and Mutable Text]]

# Java String Equality

For String references, `==` asks whether both operands designate the same object, whereas `equals` compares their character content. Interning can make two literals identical by reference, but that implementation behavior does not turn `==` into a content comparison.

A null-safe constant comparison places the known non-null string first, as in `"value".equals(candidate)`. Case-insensitive comparison uses its dedicated operation and expresses a different equivalence rule. Choosing the operation therefore depends on whether identity, exact content, or normalized content is the intended relationship.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
