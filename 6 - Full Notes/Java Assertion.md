2026-10-30 15:57

Status: #baby

Tags: [[Java Diagnostics Testing and Documentation]]

# Java Assertion

A Java `assert` statement checks an internal assumption and throws `AssertionError` when its boolean condition is false. An optional expression supplies diagnostic detail.

Assertions are disabled by default and enabled with the `-ea` launch option, so they must not perform required validation, state changes, or public-input checks. They are appropriate for conditions the program believes are already guaranteed by its own logic; ordinary exceptions enforce contracts that must remain active in production.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
