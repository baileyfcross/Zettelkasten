2026-10-30 15:57

Status: #baby

Tags: [[Java Platform Runtime and Project Structure]]

# Java Bytecode Portability

Java source is compiled into platform-neutral bytecode rather than directly into one operating system's machine instructions. A platform-specific [[Java Virtual Machine Execution Model|JVM]] then loads and executes that bytecode, so the same compiled program can run on Linux, macOS, Windows, or another supported system when a compatible runtime is present.

Portability therefore belongs to the boundary between the compiled program and its runtime. The bytecode stays the same while each JVM implementation translates or interprets it for its host machine; native libraries and operating-system assumptions can still reduce that portability.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
