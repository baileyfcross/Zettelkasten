2026-10-19 01:48

Status: #baby

Tags: [[Go Types Interfaces and Generics]]

# Go Pointer Semantics

A Go pointer stores the address of a value and has a zero value of `nil`. The address operator obtains a pointer to addressable data, the dereference operator accesses the pointed-to value, and field selection can implicitly dereference a pointer to a struct.

Pointers allow a function or method to mutate shared data without copying the entire value. Go omits general pointer arithmetic in ordinary typed code, and dereferencing `nil` produces a panic, so pointer use still requires a clear ownership and validity contract.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
