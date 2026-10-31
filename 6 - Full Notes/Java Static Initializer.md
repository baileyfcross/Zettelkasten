2026-10-31 13:15

Status: #baby

Tags: [[Java Object Construction and Class Members]]

# Java Static Initializer

A static field initializer assigns class-level state, and a static initialization block performs class-level setup that needs statements. The compiler combines this work into class initialization, which occurs for the class rather than once per object.

Static field initializers and static blocks execute in their top-to-bottom source order. Because this is a static context, the code can directly use other static members but has no current instance through which to use an instance field or method.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
