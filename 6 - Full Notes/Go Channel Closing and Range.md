2026-10-19 01:48

Status: #baby

Tags: [[Go Concurrency and Coordination]]

# Go Channel Closing and Range

Closing a Go channel declares that no more values will be sent. Receivers can continue draining buffered values, and a two-result receive indicates whether a value came before closure.

A `for range` loop receives repeatedly until the channel is both closed and drained. The sending side that owns completion should normally close the channel; sending after closure panics, and closing is not needed merely to reclaim channel memory.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
