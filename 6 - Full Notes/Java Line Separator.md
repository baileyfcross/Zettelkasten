2026-10-31 13:15

Status: #baby

Tags: [[Java System Runtime Services]]

# Java Line Separator

`System.lineSeparator()` returns the platform-dependent string used to end a line. The value is fixed from the initial `line.separator` system property and remains the same for the running process.

Unix-like systems use a newline character, while Windows uses carriage return followed by newline. Asking System for the separator avoids hard-coding one platform's sequence into text intended to remain portable.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
