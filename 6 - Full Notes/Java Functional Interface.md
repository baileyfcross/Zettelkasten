2026-10-30 15:57

Status: #baby

Tags: [[Java Streams and Functional Processing]]

# Java Functional Interface

A Java functional interface has one abstract method and can therefore be implemented by a lambda expression or method reference. Default, static, private, and inherited `Object` methods do not add abstract operations to that count.

The `@FunctionalInterface` annotation asks the compiler to verify the intended shape. Standard examples include `Predicate`, `Function`, `Consumer`, and `Supplier`, whose method signatures describe testing, transformation, consumption, and value production for stream and asynchronous APIs.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
