2026-10-30 15:57

Status: #baby

Tags: [[Java Values Strings and Core Types]]

# Java Pass-by-Value Semantics

Java passes every method argument by value. A primitive argument copies the primitive value into the parameter; an object argument copies the reference value, not the object itself.

Consequently, a method can use a copied reference to mutate the same object seen by its caller, but assigning that parameter to a different object does not replace the caller's variable. This distinction resolves the apparent contradiction between Java's value-passing rule and the visible effect of changing an object's fields inside a method.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
