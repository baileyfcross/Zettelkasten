2026-10-30 15:57

Status: #baby

Tags: [[Java Operators and Pattern Matching]]

# Java Record Pattern

A Java record pattern tests a value against a record type and destructures its components into pattern variables. Nested record patterns can follow the data structure and bind selected component values without a sequence of explicit accessor calls.

The match succeeds only when the value has the required record shape and its nested patterns succeed. This makes a record declaration useful both for construction and for transparent deconstruction in `instanceof` and `switch`, while ordinary classes remain encapsulated behind their methods.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
