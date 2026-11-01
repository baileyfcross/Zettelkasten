2026-10-31 13:27

Status: #baby

Tags: [[Kotlin Coroutines Reactive and Testing]]

# RxKotlin Observable Streams

RxKotlin adds Kotlin-oriented extensions around RxJava's reactive types. An observable represents a sequence whose values, errors, and completion are delivered to subscribers over time, allowing changing input or network data to be handled as a stream.

Operators compose stream behavior before subscription. The book demonstrates converting a list to an observable, retaining values with `filter`, removing repetitions with `distinct`, and creating periodic emissions with `interval`. Subscribers then define how to react to each signal.

# References

[[masteringkotlinforjavadevelopers.epub]]
