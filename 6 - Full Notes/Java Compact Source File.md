2026-10-30 16:54

Status: #baby

Tags: [[Java Source Launch and Documentation]]

# Java Compact Source File

A Java compact source file contains an entry method and supporting members without an explicit surrounding class declaration. The compiler creates an implicitly declared class whose name follows the source filename, reducing ceremony for small programs and beginner exercises.

The form uses the ordinary Java toolchain rather than a separate scripting dialect. It can grow incrementally with methods and fields, but it cannot declare a package; a program that needs ordinary packaging can be converted into a regular class by adding the explicit declaration and imports.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
