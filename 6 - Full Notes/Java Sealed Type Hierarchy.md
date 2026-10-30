2026-10-30 15:57

Status: #baby

Tags: [[Java Classes Interfaces and Type Declarations]]

# Java Sealed Type Hierarchy

A sealed class or interface restricts which named types may directly extend or implement it. The `permits` list defines the authorized immediate subtypes, giving the designer a controlled hierarchy without making the base type either completely final or open to every caller.

Each permitted subtype must declare how the restriction continues: it can be `final`, `sealed`, or `non-sealed`. Because the compiler knows the family, pattern matching and switch analysis can reason more precisely about exhaustiveness, while the hierarchy still supports distinct implementations.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
