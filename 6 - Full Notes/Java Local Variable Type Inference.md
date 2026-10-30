2026-10-30 15:57

Status: #baby

Tags: [[Java Values Strings and Core Types]]

# Java Local Variable Type Inference

The contextual name `var` lets the compiler infer a local variable's static type from its initializer. It shortens declarations whose type is already obvious, especially when a generic construction would otherwise repeat a long type expression.

Inference does not create a dynamically typed variable: the type is fixed at compile time, ordinary member checks still apply, and later assignments must remain compatible. `var` requires an initializer and is limited to local contexts, so fields and method signatures continue to state their types explicitly.

The later source uses `var` to remove noisy repetition around generic collections and API result types, but warns that shortening a declaration is useful only when the initializer leaves the inferred type clear. The feature changes how the type is written, not the compiler's type checks or the runtime representation.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
[[java25andbeyond_modernjavamadeeasy.epub]]
