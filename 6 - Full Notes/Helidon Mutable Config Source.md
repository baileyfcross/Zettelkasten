2026-10-19 22:48

Status: #baby

Tags: [[Helidon Configuration System]]

# Helidon Mutable Config Source

A Helidon config source is immutable by default but can expose change detection through specialized contracts. A `PollableSource` produces a signature such as a digest, timestamp, or version that can be checked periodically for change.

A `WatchableSource` delegates notification to a watcher associated with the underlying data, while an `EventConfigSource` can notify the framework directly. These mechanisms distinguish how a change is detected from how the resulting data is parsed into a new configuration tree.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
