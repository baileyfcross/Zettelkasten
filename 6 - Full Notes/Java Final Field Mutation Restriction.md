2026-10-30 16:54

Status: #baby

Tags: [[Java Platform API Evolution]]

# Java Final Field Mutation Restriction

Java's final-field mutation restriction tightens deep reflection that historically could alter some fields after normal language rules had made them final. The book's Java 26 outlook describes progressive modes that allow, warn, debug, or deny such mutation, with explicit module-level enablement for exceptional compatibility needs.

Stronger enforcement improves encapsulation and lets the JVM trust final values for optimizations such as constant folding. It does not make a referenced object immutable; it guarantees the field reference cannot be replaced through the restricted reflective path.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
