2026-10-30 16:54

Status: #baby

Tags: [[Java Platform API Evolution]]

# Java Lazy Constant

The book's Java 26 outlook renames and refines the stable-value preview as lazy constants. A lazy constant is initialized at most once, no later than first use, then remains unchanged so the JVM may apply constant-oriented optimizations.

The API extends the idea to lazily populated lists and maps whose slots initialize on demand. It retains the same boundary as [[Java Stable Value]]: use it for durable values, not mutable resources whose connection or session lifecycle must be closed and replaced.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
