2026-10-30 15:57

Status: #baby

Tags: [[Java Application Interaction and Internationalization]]

# Java Standard Input Stream

`System.in` is the process's standard input as an `InputStream`. A console launch normally connects it to the terminal, but an operating-system pipe or redirection can supply bytes from another process or file.

Reading directly exposes byte-oriented operations and requires the program to decide how bytes become characters or values. Higher-level readers and `Scanner` add decoding and tokenization. Closing a wrapper around `System.in` also closes the global stream, so a long-lived application should decide which component owns that lifecycle.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
