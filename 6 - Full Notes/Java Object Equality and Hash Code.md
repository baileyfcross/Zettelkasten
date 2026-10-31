2026-10-30 15:57

Status: #baby

Tags: [[Java Collections and Date-Time]] · [[Java Inheritance Composition and Object Contracts]]

# Java Object Equality and Hash Code

`Object.equals` defines logical equality when a class overrides its default identity comparison. A correct equality relation is reflexive, symmetric, transitive, consistent, and false for null. `hashCode` supplies a compatible integer used by hash-based collections.

Equal objects must produce equal hash codes, though unequal objects may collide. The fields used by both operations should agree and should not change while an object serves as a hash key or set element. Java records generate component-based equality and hashing automatically for their declared data.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
