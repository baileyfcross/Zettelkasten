2026-10-07 17:18

Status: #baby

Tags: [[Parallel Statistical Computing]]

# Process Rank

A process rank is the integer identity assigned to a participant within an MPI communicator. Ranks range from zero through one less than the communicator size and let the same program select different work for different processes.

Rank zero is often used as a coordinator, but this is a program convention rather than an MPI requirement. Messages name source and destination ranks, and a data partition can use rank as an index so each process receives a reproducible portion of the workload.

# References

[[statisticalcomputingincplusplusandr.pdf]]
