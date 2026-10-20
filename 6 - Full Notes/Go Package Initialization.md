2026-10-19 01:48

Status: #baby

Tags: [[Go Program Structure and Toolchain]]

# Go Package Initialization

A Go package may define multiple `init` functions that run before the program's `main` function. Package initialization occurs once even when several source files or downstream packages import the same package.

A blank [[Go Import Declaration|import]] can request these initialization effects without binding exported names. Because this hides behavior behind an import, it is best reserved for packages whose documented purpose includes registration or another required startup effect.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
