2026-10-19 01:48

Status: #baby

Tags: [[Go Types Interfaces and Generics]]

# Go Function Values and Closures

Functions are first-class Go values: they can be assigned, passed as arguments, returned, and stored in fields or collections. A function literal can capture variables from its lexical environment and continue accessing them after the declaring call returns.

Captured variables remain shared state rather than immutable snapshots, so a closure may both read and update them. This supports callbacks and factories but requires synchronization if concurrent goroutines access the same captured value.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
