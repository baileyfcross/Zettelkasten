2026-10-30 15:57

Status: #baby

Tags: [[Java Concurrency and Reactive Streams]]

# Reactive Streams Backpressure

Backpressure lets a reactive consumer control how much data an upstream producer may send. In Java Flow, the subscriber receives a `Subscription` and calls `request(n)` to establish demand; the publisher must not emit more `onNext` signals than have been requested.

Demand is a protocol, not a magical buffer strategy. The system still needs policies for slow consumers, bounded queues, cancellation, and failure. Requesting one element after each successful consumption makes the rate relationship visible, while requesting unbounded demand deliberately gives up downstream pacing.

The Spring Boot discussion applies backpressure to database rows and RSocket streams. An R2DBC repository can expose a large result as Flux while the downstream subscriber controls demand, and RSocket carries that demand across a persistent connection. Operators such as rate limiting are still needed when the producer can outpace the final client or when an intermediate buffer is bounded.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
