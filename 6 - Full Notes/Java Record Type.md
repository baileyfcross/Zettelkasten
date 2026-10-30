2026-10-30 15:57

Status: #baby

Tags: [[Java Classes Interfaces and Type Declarations]]

# Java Record Type

A Java record is a compact class declaration for data whose identity is determined by a fixed list of components. The compiler supplies private final fields, component accessors, a canonical constructor, and value-oriented `equals`, `hashCode`, and `toString` implementations.

Records are shallowly immutable: component references cannot be reassigned, but referenced mutable objects can still change. A compact canonical constructor can validate or normalize incoming values. Records can implement interfaces and define additional members, but they are final and cannot extend another application class.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
