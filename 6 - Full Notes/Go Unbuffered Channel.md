2026-10-19 01:48

Status: #baby

Tags: [[Go Concurrency and Coordination]]

# Go Unbuffered Channel

An unbuffered Go channel has zero capacity, so a send cannot complete until a receiver is ready and a receive cannot complete until a sender is ready. The exchange synchronizes the participating goroutines while transferring one typed value.

This lockstep behavior can establish a required processing order without an explicit mutex. It can also deadlock when no complementary operation can run, especially when one goroutine attempts both sides of the exchange sequentially.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
