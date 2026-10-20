2026-10-19 01:48

Status: #baby

Tags: [[Go Concurrency and Coordination]]

# Go Once Initialization

Go's `sync.Once` runs a supplied function no more than one time even when multiple goroutines call `Do` concurrently. Later calls return without executing the function again.

This supports lazy shared initialization without manually combining a flag and lock. The one-time function should establish a complete usable state because a panic does not make the same `Once` retry that function on a later call.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
