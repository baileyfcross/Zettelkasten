2026-10-31 13:15

Status: #baby

Tags: [[Java Object Construction and Class Members]]

# Java Utility Class

A Java utility class groups operations and values that belong to the class rather than to individual objects. Its members are static, so callers select them through the class name without constructing an instance; `java.lang.Math` and `java.lang.System` follow this organization.

This form is suitable when no per-object state is required. Static fields are shared across every caller, so mutable class state also creates shared coupling, whereas static methods that depend only on their arguments act as reusable named operations.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
