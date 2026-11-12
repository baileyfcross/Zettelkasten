2026-11-11 18:27

Status: #baby

Tags: [[Parallel Program Design]]

# Concurrency and Parallelism

Concurrency is a property of a solution that permits parts of the work to make progress independently, while parallelism is the execution of such work at the same time on multiple processing elements. A concurrent algorithm can run through interleaving on one processor without achieving parallel speedup.

Design must expose operations without blocking dependencies before hardware can execute them simultaneously. The distinction prevents a thread-based implementation from being assumed faster merely because its activities are concurrent.

# References

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]

