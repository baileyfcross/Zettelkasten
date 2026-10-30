2026-10-30 15:57

Status: #baby

Tags: [[Java Concurrency and Reactive Streams]]

# Java Flow Subscription

`Flow.Subscription` is the control link between one publisher and one subscriber. `request(long)` increases permitted demand, while `cancel` ends the relationship and tells the publisher that no more elements are wanted.

The subscriber receives this link before any item and must retain it to request later work. Invalid demand or signals that exceed demand violate the protocol. A subscription therefore carries control upstream while data, completion, and error signals move downstream.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
