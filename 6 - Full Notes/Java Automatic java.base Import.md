2026-10-30 16:54

Status: #baby

Tags: [[Java Source Launch and Documentation]]

# Java Automatic java.base Import

An implicitly declared Java class automatically imports the public types exported by the `java.base` module. Collections, streams, date-time types, file utilities, and other core APIs are therefore available to a compact source program without explicit package imports.

The rule expands on Java's longstanding automatic availability of `java.lang`. It is aimed at progressive learning and small programs; when converted to an ordinary class, the programmer adds the explicit imports that document the same dependencies.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
