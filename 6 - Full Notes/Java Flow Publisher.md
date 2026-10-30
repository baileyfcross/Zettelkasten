2026-10-30 15:57

Status: #baby

Tags: [[Java Concurrency and Reactive Streams]]

# Java Flow Publisher

`Flow.Publisher<T>` is the source-side Reactive Streams interface in the JDK. Its `subscribe` method accepts a subscriber and begins establishing a relationship through which signals can be delivered under a subscription's demand.

A publisher must respect signal order, demand, cancellation, and terminal completion or error. Producing values is not enough: it must provide a valid subscription before sending data and stop after a terminal signal. `SubmissionPublisher` offers one JDK implementation for asynchronous submission and buffering.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
