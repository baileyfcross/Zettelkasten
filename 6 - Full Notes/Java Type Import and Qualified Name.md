2026-10-31 13:15

Status: #baby

Tags: [[Java Nested Types and Package Organization]]

# Java Type Import and Qualified Name

A fully qualified Java type name includes its package sequence, as in `java.lang.System`. An `import` declaration tells the compiler which package supplies an unqualified type name so the source can use the shorter simple name without copying or loading code at the declaration.

An import can name one type or use a wildcard for the types in one package. Wildcards do not import nested subpackages and can make same-named types ambiguous, in which case a fully qualified name disambiguates the reference. Types in `java.lang` are imported automatically.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
