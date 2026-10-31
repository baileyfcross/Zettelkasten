2026-10-31 13:15

Status: #baby

Tags: [[Java Nested Types and Package Organization]]

# Java Static Import

A Java static import makes one named static member, or all static members of a named type, available without the type-name prefix. It can import both constants and static methods.

The feature avoids implementing a constant-only interface merely to inherit unqualified names. Importing same-named members from different types creates ambiguity, and importing too many names can conceal their ownership, so the shorter spelling trades some explicit context for convenience.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
