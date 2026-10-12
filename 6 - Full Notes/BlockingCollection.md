2026-09-27 00:11

Status: #baby

Tags: [[.NET Concurrent Collections and Lazy Initialization]]

# BlockingCollection

`BlockingCollection<T>` wraps a producer-consumer collection with optional bounded capacity and blocking add and take operations. Producers can wait when the collection is full, consumers can wait when it is empty, and completion signals that no more items will arrive.

Bounded capacity supplies backpressure so fast producers cannot grow memory use without limit. Cancellation and completion must be coordinated so blocked participants can leave cleanly during shutdown.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
