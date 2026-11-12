2026-11-11 18:27

Status: #baby

Tags: [[Parallel Program Design]]

# Manager-Worker Pattern

The Manager-Worker pattern gives one coordinating component responsibility for distributing independent work items among a set of workers. Workers perform the assigned computation and return results, while the manager tracks availability and completion.

Dynamic assignment can balance uneven task durations better than a fixed partition, but the manager can become a communication or scheduling bottleneck. The pattern fits an [[Embarrassingly Parallel Problem]] when tasks are independent and the coordination cost is small relative to their computation.

# References

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]

