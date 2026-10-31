2026-10-31 13:15

Status: #baby

Tags: [[Java System Runtime Services]]

# Java System Standard Output

`System.out` is the process's standard non-error output as a `PrintStream`. It normally targets the console screen, while the program writes through overloaded `print` and `println` methods without needing to know the ultimate destination.

`println` adds the platform's line separator after its argument, and its no-argument form writes a blank line. Standard output can be redirected independently of [[Java System Standard Error]], preserving a channel for ordinary results while diagnostics go elsewhere.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
