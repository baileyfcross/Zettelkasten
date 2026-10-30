2026-10-30 16:54

Status: #baby

Tags: [[Java Collection and Stream Evolution]]

# Java Stream toList Terminal Operation

`Stream.toList()` is a concise terminal operation that materializes stream elements as a list. It replaces the longer `collect(Collectors.toList())` form when the result is not intended to be mutated.

The two forms are not interchangeable in every program: `toList()` returns an unmodifiable list, while the collector form used in the book produces a mutable list. Choosing the shorter operation therefore also chooses an immutability contract for downstream code.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
