2026-11-06 13:25

Status: #baby

Tags: [[Java Collections and Date-Time]]

# Java ArrayList Capacity Growth

Java `ArrayList` separates logical size from backing-array capacity. A no-argument list begins with shared empty storage, allocates its element array when the first item is added, and creates a larger array when the current capacity is exhausted.

In the implementation described by the source, growth is approximately 1.5 times the previous capacity. A resize copies $n$ existing references and is therefore $O(n)$, but because it occurs only occasionally, repeated appends have amortized $O(1)$ cost.

Supplying an expected initial capacity can avoid repeated copies during bulk insertion without changing the list's logical size. `trimToSize()` can release unused capacity, but it also copies the live elements and may cause another growth cycle if additions resume.

# References

[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
