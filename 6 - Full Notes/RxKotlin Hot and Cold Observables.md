2026-10-31 13:27

Status: #baby

Tags: [[Kotlin Coroutines Reactive and Testing]]

# RxKotlin Hot and Cold Observables

The book distinguishes cold streams, which begin producing values when a subscriber or collector starts them, from hot streams, which can emit independently of a particular collector. The distinction determines whether each consumer initiates a data flow or joins an already active one.

Kotlin `Flow` is presented as a cold stream: its builder describes emissions, operators transform them, and collection starts the work. Choosing a hot or cold form therefore changes the lifetime and sharing relationship between the producer and its consumers.

# References

[[masteringkotlinforjavadevelopers.epub]]
