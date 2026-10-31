2026-10-31 13:15

Status: #baby

Tags: [[Java Object Construction and Class Members]]

# Java Final Instance Field Initialization

A blank final instance field is declared without an initializer and assigned during construction. Every constructor path must establish its value once before the new object becomes available, and later reassignment is prohibited.

This permits constructor arguments to determine immutable per-object state while preserving the one-assignment rule. It differs from a `static final` constant, whose single value belongs to the class and is shared by all instances.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
