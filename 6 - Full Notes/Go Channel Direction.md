2026-10-19 01:48

Status: #baby

Tags: [[Go Concurrency and Coordination]]

# Go Channel Direction

Go channel types can be bidirectional, send-only, or receive-only. A channel is commonly created for both directions and then passed through a narrower function parameter that exposes only the operation the function is meant to perform.

Direction is a compile-time capability boundary: a producer accepting `chan<- T` cannot receive, and a consumer accepting `<-chan T` cannot send. This documents pipeline roles and prevents accidental misuse without changing the underlying channel.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
