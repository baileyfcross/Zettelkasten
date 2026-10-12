2026-09-27 00:11

Status: #baby

Tags: [[.NET Concurrent Collections and Lazy Initialization]]

# IProducerConsumerCollection

`IProducerConsumerCollection<T>` defines concurrent insertion and removal operations for collections that can sit between producers and consumers. Queues, stacks, and bags can implement the same handoff contract while retaining different retrieval policies.

The interface lets a higher-level coordinator depend on safe transfer rather than a concrete ordering strategy. It does not itself add blocking or bounded capacity; `BlockingCollection<T>` supplies those behaviors around an implementation.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
