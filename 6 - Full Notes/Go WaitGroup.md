2026-10-19 01:48

Status: #baby

Tags: [[Go Concurrency and Coordination]]

# Go WaitGroup

A Go WaitGroup is a counter used to wait for a set of goroutines to finish. The launching goroutine increments the counter before each launch, workers call `Done` when exiting, and `Wait` blocks until the count reaches zero.

Incrementing before launch avoids a race in which waiting begins before the worker registers itself. A deferred `Done` keeps completion accounting on paths that return early, but the WaitGroup carries neither worker results nor errors; those need a separate channel or shared structure.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
