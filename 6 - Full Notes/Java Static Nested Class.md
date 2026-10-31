2026-10-31 13:15

Status: #baby

Tags: [[Java Nested Types and Package Organization]]

# Java Static Nested Class

A static nested class is declared as a static member inside an enclosing class. Its name is qualified by the enclosing class, and it can have a more restrictive member access level than a top-level class.

Like a static method, it has no implicit enclosing object. It can directly access static members of the enclosing class, including private ones, but needs an object reference to reach that class's instance members. This makes it behave much like a top-level helper placed inside another type for organization and encapsulation.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
