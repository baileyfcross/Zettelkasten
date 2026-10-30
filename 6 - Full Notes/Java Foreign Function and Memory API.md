2026-10-30 16:54

Status: #baby

Tags: [[Java Low-Level Platform and Native Performance]]

# Java Foreign Function and Memory API

Java's Foreign Function and Memory API provides typed access to native functions and memory outside the JVM. It offers a standard alternative to the ceremony of JNI and the process-corrupting risk of unrestricted `sun.misc.Unsafe` access.

Foreign calls combine a symbol lookup, linker, function descriptor, and method handle. Foreign data is represented through bounded memory segments whose lifetime is controlled by an arena, making native interoperability more explicit about types, ownership, and cleanup.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
