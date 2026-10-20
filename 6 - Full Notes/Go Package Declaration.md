2026-10-19 01:48

Status: #baby

Tags: [[Go Program Structure and Toolchain]]

# Go Package Declaration

Every Go source file begins with a package declaration that assigns the file to a package. Files in the same directory that declare the same package are compiled together, so top-level types, variables, constants, and functions can be distributed across several files.

The declaration precedes imports and other declarations. A child package is independent of its parent despite its directory placement, and code outside a package can use its exported identifiers only after importing the package.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
