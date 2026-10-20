2026-10-19 01:48

Status: #baby

Tags: [[Go Types Interfaces and Generics]]

# Go Slice Capacity and Append

A slice's length counts accessible elements, while its capacity bounds how far that view can grow in the current backing array. `make` can establish both values independently when reserving space for later additions.

The built-in `append` returns the updated slice and may allocate a larger backing array when capacity is exhausted. Callers must assign that return value because the original descriptor does not acquire a replacement array merely by being passed to `append`.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
