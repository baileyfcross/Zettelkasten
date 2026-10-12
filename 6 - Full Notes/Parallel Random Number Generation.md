2026-10-07 17:18

Status: #baby

Tags: [[Parallel Statistical Computing]] [[Pseudorandom Number Generation Methods]]

# Parallel Random Number Generation

Parallel random number generation gives each worker a stream that is individually high quality and has minimal dependence on every other worker's stream. Simply seeding identical generators with nearby values does not by itself establish those properties.

Two approaches are parameterization, where workers receive different generator parameters, and sequence splitting, where one very long period is partitioned into nonoverlapping substreams. A useful scheme should scale to many processors without moving generated data between them and should preserve reproducibility when the worker-stream assignment is recorded.

# References

[[statisticalcomputingincplusplusandr.pdf]]
