2026-10-30 16:54

Status: #baby

Tags: [[Java Records Patterns and Construction]]

# Java Generic Record Pattern Inference

Java generic record-pattern inference lets the compiler determine component types while deconstructing a generic record, including nested records. Pattern variables can be declared with `var` and still retain the concrete operations supplied by the inferred type.

This removes repeated type arguments from a [[Java Record Pattern]] without falling back to an unsafe raw deconstruction. It is especially useful when the surrounding generic structure already contains enough information for the compiler to infer each nested component.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
