2026-11-11 18:27

Status: #baby

Tags: [[Parallel Program Design]]

# Single Program Multiple Data

Single Program Multiple Data is a program structure in which several processing elements run copies of the same program over different portions of a dataset. Each copy may follow a different control path, so the workers do not have to remain in lockstep as they would in a strict SIMD execution model.

The structure simplifies deploying one codebase across workers, but each worker needs a way to identify its data partition and coordinate shared or exchanged results. Partition balance and communication still determine whether additional workers improve elapsed time.

# References

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]

