2026-10-30 15:57

Status: #baby

Tags: [[Java Concurrency and Reactive Streams]]

# Java Flow Processor

`Flow.Processor<T,R>` is both a subscriber of input values and a publisher of output values. It can filter, transform, or otherwise mediate a stream while receiving upstream demand control and establishing its own downstream subscription.

The dual role requires propagation in both directions: data and terminal signals move toward consumers, while demand and cancellation must influence upstream production. A processor that transforms integers into characters, for example, receives integer signals, applies its function, submits character signals, and requests the next input according to its policy.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
