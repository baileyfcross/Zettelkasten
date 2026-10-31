2026-10-31 13:15

Status: #baby

Tags: [[Java System Runtime Services]]

# Java Standard I-O Redirection

Standard I/O lets a Java program communicate through input, normal output, and error channels without depending on one concrete device. A command shell can redirect input from a file with `<`, normal output with `>`, and standard error with its separate stream identifier.

The System class also provides `setIn`, `setOut`, and `setErr` to replace the corresponding streams inside the process. This indirection lets the same reading or printing code operate against a console, file, or another stream destination.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
