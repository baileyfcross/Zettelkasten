2026-10-30 15:57

Status: #baby

Tags: [[Java Classes Interfaces and Type Declarations]]

# Java Enum Type

A Java enum declares a closed set of named instances. The instances are created by the enum declaration, external code cannot construct more, and every enum implicitly extends `java.lang.Enum`, which supplies identity, name, ordinal, and lookup behavior.

An enum can contain fields, methods, and a private constructor, so each constant can carry associated data or behavior. It cannot extend another class, but it can implement interfaces. Enum values work naturally in `switch` because the compiler knows the permitted set.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
