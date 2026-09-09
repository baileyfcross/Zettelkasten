2026-09-08 21:16

Status: #baby

Tags: [[.NET Assemblies Packages and Deployment]]

# Intermediate Language

A .NET language compiler translates source code into intermediate language instructions stored in an assembly. The runtime loads that assembly and compiles the IL into native instructions for the current processor before execution.

This intermediate representation separates the source language from the machine architecture. Different .NET languages can target the same runtime services, and one compiled assembly can remain portable where a compatible runtime supplies the required APIs.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
