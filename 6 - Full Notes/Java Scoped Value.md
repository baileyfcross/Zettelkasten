2026-10-30 16:54

Status: #baby

Tags: [[Java Structured Concurrency and Scoped Context]]

# Java Scoped Value

A Java scoped value provides immutable contextual data during a bounded dynamic execution. Request users, trace identifiers, locales, or timestamps can be read by downstream code without being threaded through every intermediate method signature.

The binding exists only inside the action opened for it and can be inherited by child tasks in that scope. This bounded lifetime and immutability distinguish scoped context from a mutable global variable and make it particularly suitable for short-lived virtual-thread work.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
