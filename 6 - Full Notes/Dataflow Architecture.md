2026-09-06 21:16

Status: #baby

Tags: [[Augmented Reality Software Architecture]]

# Dataflow Architecture

A dataflow architecture expresses computation as components connected by the movement of data. A source produces measurements, filters transform them, and consumers use the resulting values for simulation, interaction, or rendering.

The structure suits AR pipelines because components can be developed and tested separately, then connected locally or across hosts. Scheduling and buffering must preserve acceptable latency and ensure that data dependencies update coherently.

# References

[[augmentedreality_pearson.pdf]]
