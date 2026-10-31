2026-10-31 13:15

Status: #baby

Tags: [[Java Inheritance Composition and Object Contracts]]

# Java Forwarding Method

A forwarding method presents an operation on a wrapper and delegates the corresponding work to a composed object stored in a private field. The wrapper can perform additional behavior before or after delegation without extending the wrapped class.

Forwarding makes the exposed surface explicit: only declared wrapper methods are available, and a change in the wrapped class's internal method calls does not silently alter the wrapper's behavior. It is the operational companion to [[Java Composition over Inheritance]].

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
