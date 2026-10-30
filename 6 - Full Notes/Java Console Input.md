2026-10-30 15:57

Status: #baby

Tags: [[Java Application Interaction and Internationalization]]

# Java Console Input

`System.console()` returns a `Console` when the process has an attached interactive console and may return null under an IDE or redirected launch. The object supports formatted prompts, line reading, and password reading without echoing the characters.

Password input is returned as a character array so the caller can overwrite sensitive data after use rather than leaving an immutable String in memory. Code must still handle the absent-console case and should not assume that every execution environment offers an interactive terminal.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
