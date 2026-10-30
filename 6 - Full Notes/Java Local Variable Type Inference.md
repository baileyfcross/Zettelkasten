2026-10-30 15:57

Status: #baby

Tags: [[Java Values Strings and Core Types]]

# Java Local Variable Type Inference

The contextual name `var` lets the compiler infer a local variable's static type from its initializer. It shortens declarations whose type is already obvious, especially when a generic construction would otherwise repeat a long type expression.

Inference does not create a dynamically typed variable: the type is fixed at compile time, ordinary member checks still apply, and later assignments must remain compatible. `var` requires an initializer and is limited to local contexts, so fields and method signatures continue to state their types explicitly.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
