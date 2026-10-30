2026-10-30 15:57

Status: #baby

Tags: [[Java Values Strings and Core Types]]

# Java Diamond Operator

The Java diamond operator, `<>`, asks the compiler to infer constructor type arguments from the surrounding generic declaration or target context. It removes repeated type names while preserving the same compile-time generic type.

For example, the right side of a variable initialization can construct an `ArrayList<>` when the left side already states the element type. The diamond does not remove generics or make the collection untyped; it merely omits redundant source syntax after the compiler has enough information to infer the arguments.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
