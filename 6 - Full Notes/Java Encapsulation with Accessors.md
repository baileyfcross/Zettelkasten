2026-10-30 15:57

Status: #baby

Tags: [[Java Classes Interfaces and Type Declarations]] · [[Java Object Construction and Class Members]]

# Java Encapsulation with Accessors

Encapsulation keeps an object's representation behind methods that define the permitted operations. A common Java form makes fields private and exposes getters and setters, allowing validation, derived values, or read-only access to be added without making every caller manipulate the field directly.

An accessor is not automatically good encapsulation: a public setter that accepts every value merely relocates direct assignment. The useful boundary states an invariant, such as rejecting an invalid age or omitting a setter for immutable state. Boolean getters conventionally use an `is` prefix when they represent a property.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
