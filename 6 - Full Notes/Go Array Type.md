2026-10-19 01:48

Status: #baby

Tags: [[Go Types Interfaces and Generics]]

# Go Array Type

A Go array is a fixed-length, zero-indexed sequence whose length is part of its type. `[10]int` and `[20]int` are therefore distinct types even though their element type is the same.

Assigning or passing an array copies its elements rather than creating an alias to the same array. Direct array use is less common than [[Go Slice Descriptor|slices]]; a slice can provide a view over an array when shared access and variable length are more useful.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
