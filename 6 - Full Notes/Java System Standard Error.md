2026-10-31 13:15

Status: #baby

Tags: [[Java System Runtime Services]]

# Java System Standard Error

`System.err` is the process's standard error destination as a `PrintStream`. It normally appears on the console, but the operating system can redirect it separately from `System.out`.

Writing usage failures and other error-oriented messages to this stream keeps them distinct from a program's normal output. The separation lets a caller save or pipe ordinary results while still displaying errors, or capture the error stream in its own file.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
