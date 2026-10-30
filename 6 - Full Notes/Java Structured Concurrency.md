2026-10-30 15:57

Status: #baby

Tags: [[Java Concurrency and Reactive Streams]]

# Java Structured Concurrency

Structured concurrency treats a group of related concurrent tasks as one lexical operation. A scope forks subtasks, waits or joins according to a policy, propagates failure or cancellation, and closes only after its children have reached an allowed outcome.

The structure makes task lifetime resemble block structure: child work cannot silently outlive the request that created it. In the book's Java 23 context the API remained a preview feature, so it requires preview flags and should be treated as version-specific while preserving the underlying principle of bounded concurrent lifetimes.

The Java 25 fifth preview organizes result policy around joiners. A scope may return the first successful result, require every subtask to succeed, or use a custom thread-safe joiner; nested scopes keep secondary task lifetimes inside their parent tasks. Exiting the structure accounts for every child through completion or cancellation.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
[[java25andbeyond_modernjavamadeeasy.epub]]
