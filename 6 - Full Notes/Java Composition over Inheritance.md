2026-10-31 13:15

Status: #baby

Tags: [[Java Inheritance Composition and Object Contracts]]

# Java Composition over Inheritance

Java inheritance models an is-a relationship, whereas composition gives one object fields that refer to the other objects forming its parts and models a has-a relationship. A class can use both when it is genuinely a specialized superclass and also contains collaborating components.

Composition avoids depending on undocumented implementation details in a superclass. If an inherited implementation calls overridable methods or later gains a method that collides with a subclass declaration, subclass behavior can break; wrapping the reusable object behind a field limits that fragile-base-class coupling.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
