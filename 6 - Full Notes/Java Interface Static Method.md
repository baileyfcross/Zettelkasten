2026-10-31 13:15

Status: #baby

Tags: [[Java Inheritance Composition and Object Contracts]]

# Java Interface Static Method

A Java interface can declare a static method whose implementation belongs to the interface itself. Callers qualify the method with the interface name rather than with an implementing class or an object.

This placement associates a utility operation directly with the contract it supports. Unlike an abstract interface method, it is not an instance operation that implementing classes override, and it is not inherited as though it were a static member of those classes.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
