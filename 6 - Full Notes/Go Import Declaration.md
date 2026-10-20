2026-10-19 01:48

Status: #baby

Tags: [[Go Program Structure and Toolchain]]

# Go Import Declaration

A Go import declaration makes another package's exported identifiers available to one source file. References remain qualified by the imported package name, and an alias can replace the final component of the import path when a different local name is useful.

Imports are file-scoped, must appear after the [[Go Package Declaration]], and normally must be used. A blank alias imports a package only for initialization side effects, while ordinary imports expose the package's public surface without importing individual identifiers.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
