2026-10-31 22:04

Status: #baby

Tags: [[Java Vector Masks and Data Movement]]

# Java Vector Gather Operation

A Java vector gather loads lanes from memory addresses selected by an index map rather than from one contiguous region. It enables table lookup, memoized-state retrieval, and structure-like access when required values are scattered.

Gather is less regular than an ordinary vector load. Address calculation, cache behavior, and missing locality can serialize or stall the operation, and the Java API may require auxiliary index arrays or conversions. The book uses gather where previous Collatz orbit lengths or indexed sliding-window values cannot be loaded sequentially.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
