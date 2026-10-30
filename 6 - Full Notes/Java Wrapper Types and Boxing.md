2026-10-30 15:57

Status: #baby

Tags: [[Java Values Strings and Core Types]]

# Java Wrapper Types and Boxing

Each Java primitive has a corresponding reference wrapper, such as `Integer` for `int` and `Boolean` for `boolean`. Wrappers supply parsing, conversion, comparison, bounds, and other operations and allow primitive-like values to be used where an object type or generic parameter is required.

Autoboxing converts a primitive to its wrapper and unboxing extracts the primitive value automatically. These conversions are convenient but can allocate objects, and unboxing a null wrapper throws a `NullPointerException`. Wrapper identity should not be used as a substitute for numeric or logical value equality.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
