2026-10-30 15:57

Status: #baby

Tags: [[Java Streams and Functional Processing]]

# Java Method Reference

A Java method reference is a compact functional value for a lambda whose body delegates directly to an existing method or constructor. Forms can reference a static method, an instance method on a particular object, an instance method on a supplied receiver, or a constructor.

The compiler matches the referenced member to the target functional interface's parameters and result. `System.out::println`, for example, can replace a one-argument lambda that only calls `println`. A reference improves clarity when it names the actual operation; a lambda remains clearer when arguments must be rearranged or additional logic is required.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
