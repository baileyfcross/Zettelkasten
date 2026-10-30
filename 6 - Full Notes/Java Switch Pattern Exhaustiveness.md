2026-10-30 16:54

Status: #baby

Tags: [[Java Records Patterns and Construction]]

# Java Switch Pattern Exhaustiveness

Java switch-pattern exhaustiveness is the compiler's proof that every permitted input has a matching case. Enums and [[Java Sealed Type Hierarchy|sealed hierarchies]] give the compiler a closed set of alternatives, allowing a switch expression to omit a catch-all `default` when each alternative is covered.

The guarantee depends on compiling the switch against the current hierarchy. If a permitted subtype or enum constant changes without recompiling dependent code, runtime matching can fail rather than silently invent a result. Exhaustiveness therefore complements, but does not replace, coherent builds.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
