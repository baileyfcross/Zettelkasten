2026-10-04 22:20

Status: #baby

Tags: [[R Package Workspace and System Operations]]

# R Package Unloading

R package unloading detaches an attached package from the search path and, when possible, unloads its namespace. Detaching removes direct lookup of exported names, but dependent packages, registered methods, or remaining namespace references may prevent a complete reversal of the package's effects.

A fresh session is often safer when testing whether code truly works without the package. Unloading should not be confused with uninstalling, which removes package files from the library.

# References

[[rprimer.pdf]]
