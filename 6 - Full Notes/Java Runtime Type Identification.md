2026-10-31 13:15

Status: #baby

Tags: [[Java Inheritance Composition and Object Contracts]]

# Java Runtime Type Identification

Java runtime type identification examines the actual class of an object while a program runs. The JVM performs it when checking an explicit reference cast, and the `instanceof` operator exposes a Boolean test that code can use before a potentially unsafe downcast.

An object created from a subclass also satisfies `instanceof` tests for its superclasses and implemented interfaces. Repeatedly branching on concrete types can signal that [[Java Late Method Binding]] would express the behavior more directly through overridden methods.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
