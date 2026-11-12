2026-11-11 18:27

Status: #baby

Tags: [[Parallel Program Design]]

# Parallel Design Space

A parallel design space separates the creation of a parallel program into related decisions: finding concurrency, selecting an algorithm structure, choosing supporting program and data structures, and mapping them to implementation mechanisms such as threads, synchronization, and communication.

The separation keeps a hardware API from deciding the algorithm too early. A designer first decomposes tasks or data and analyzes dependencies, then evaluates structures such as task parallelism, pipelines, shared queues, or distributed arrays before committing to a particular runtime.

# References

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]

