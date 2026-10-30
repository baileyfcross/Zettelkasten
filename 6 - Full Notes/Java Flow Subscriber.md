2026-10-30 15:57

Status: #baby

Tags: [[Java Concurrency and Reactive Streams]]

# Java Flow Subscriber

`Flow.Subscriber<T>` consumes Reactive Streams signals through `onSubscribe`, `onNext`, `onError`, and `onComplete`. It stores the accepted subscription, requests demand, processes each value, and treats error or completion as terminal.

The subscriber drives whether work can flow by requesting elements. It must avoid accepting conflicting subscriptions and should cancel an unwanted one. No useful processing begins until the flow is subscribed, which makes subscription the activation boundary between a declared component graph and an executing stream.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
