2026-10-30 15:57

Status: #baby

Tags: [[Java Concurrency and Reactive Streams]]

# Project Reactor Flux and Mono

Project Reactor supplies higher-level Reactive Streams publishers and operators. `Flux<T>` represents a sequence of zero or more elements, while `Mono<T>` represents zero or one, and both can be transformed, filtered, combined, observed, and subscribed without manually implementing every Flow interface.

Reactor manages demand and nonblocking composition more practically than the JDK's minimal interfaces, but the same end-to-end constraint remains: inserting a blocking operation into the chain can stall its execution model. The declared pipeline stays inactive until subscription establishes a consumer.

The Spring Boot source uses `Mono` for zero-or-one results and `Flux` for zero-to-many streams in WebFlux and R2DBC. Operators can combine independent results, recover from selected errors, filter streams, or wrap legacy blocking work on an appropriate scheduler. Subscription remains the terminal trigger, and calling `block` inside the event-loop path defeats the nonblocking model.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
