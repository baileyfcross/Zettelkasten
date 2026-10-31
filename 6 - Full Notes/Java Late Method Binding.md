2026-10-31 13:15

Status: #baby

Tags: [[Java Inheritance Composition and Object Contracts]]

# Java Late Method Binding

Late binding selects an overridden non-final instance method from the receiver's runtime class. A variable may have a superclass type, yet invoking an overridden method through it executes the subclass implementation belonging to the object actually referenced.

The compiler checks that the method exists in the declared type and that the call's arguments are valid, then emits a call whose final target is chosen at runtime. Static, final, and otherwise non-polymorphic calls can be bound without this runtime selection.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
