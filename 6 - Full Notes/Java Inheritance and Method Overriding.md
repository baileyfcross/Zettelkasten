2026-10-30 15:57

Status: #baby

Tags: [[Java Classes Interfaces and Type Declarations]] · [[Java Inheritance Composition and Object Contracts]]

# Java Inheritance and Method Overriding

Java class inheritance lets one subclass extend one direct superclass, inheriting accessible members and specializing behavior. A subclass constructor invokes a superclass constructor, and `super` can select the parent implementation or constructor when the subclass needs to add rather than replace behavior.

Overriding supplies a new implementation with a compatible signature and return type. Dynamic dispatch chooses the implementation from the object's runtime type even when the reference has a superclass type. `@Override` asks the compiler to verify the intended relationship, while `final` can prevent a method or class from being extended further.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
