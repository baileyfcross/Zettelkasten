2026-10-31 13:15

Status: #baby

Tags: [[Java Inheritance Composition and Object Contracts]]

# Java Upcasting and Downcasting

Upcasting assigns a subtype reference to a supertype variable. It is implicit because every instance of the subtype is also an instance of its superclass or implemented interface, but the resulting expression exposes only the operations declared by that supertype.

Downcasting explicitly converts a supertype reference back to a subtype. The compiler can allow a cast within the same hierarchy even when the referenced object has the wrong runtime type, so the JVM verifies it and throws `ClassCastException` when the object is not an instance of the requested subtype. [[Java Runtime Type Identification]] can guard the operation.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
