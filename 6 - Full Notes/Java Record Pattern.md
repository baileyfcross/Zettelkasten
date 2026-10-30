2026-10-30 15:57

Status: #baby

Tags: [[Java Operators and Pattern Matching]]

# Java Record Pattern

A Java record pattern tests a value against a record type and destructures its components into pattern variables. Nested record patterns can follow the data structure and bind selected component values without a sequence of explicit accessor calls.

The match succeeds only when the value has the required record shape and its nested patterns succeed. This makes a record declaration useful both for construction and for transparent deconstruction in `instanceof` and `switch`, while ordinary classes remain encapsulated behind their methods.

Nested patterns can follow several record layers in one match, and generic record patterns can infer component types from the matched record. A null record value does not match, although a component extracted from a successful outer record match can itself be null when its component pattern permits that value.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
[[java25andbeyond_modernjavamadeeasy.epub]]
