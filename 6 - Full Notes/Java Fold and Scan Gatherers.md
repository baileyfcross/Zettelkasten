2026-10-30 16:54

Status: #baby

Tags: [[Java Collection and Stream Evolution]]

# Java Fold and Scan Gatherers

Java's predefined `fold` and `scan` gatherers both carry state across a stream. `fold` combines all inputs into one emitted aggregate, while `scan` emits the updated aggregate after every input and therefore exposes every intermediate result.

A fold can produce a final sum or product and still remain inside a stream pipeline; a scan can produce cumulative daily expenses or running text. The distinction is cardinality: fold is many-to-one, whereas scan is one-to-one after initialization.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
