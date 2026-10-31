2026-10-31 13:15

Status: #baby

Tags: [[Java String Processing and Mutable Text]]

# Java StringBuffer

`java.lang.StringBuffer` represents a mutable sequence of characters. Unlike a String, its contents can be changed after construction through operations such as append, insert, delete, reverse, and indexed character replacement.

The buffer tracks both length and capacity. Length counts the stored characters, while capacity is the maximum that fits before a larger internal array must replace the current one. Constructors can use the default initial capacity, a requested capacity, or initial String content, and `toString()` produces an immutable String from the current sequence.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
