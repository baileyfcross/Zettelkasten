2026-10-19 01:48

Status: #baby

Tags: [[Go Concurrency and Coordination]]

# Go Buffered Channel

A buffered Go channel stores a bounded number of sent values before requiring a receiver. A send blocks only when the buffer is full, while a receive blocks when it is empty.

Capacity therefore changes how independently producers and consumers can progress and can materially alter observed interleaving. A buffer is not unlimited queue storage or an automatic cure for deadlock; its size should express a deliberate bound on in-flight work or results.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
