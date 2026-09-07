2026-09-06 22:42

Status: #baby

Tags: [[Large-Scale Graph Processing]]

# Pregel

Pregel is a distributed graph-processing model built around vertex-centric computation in synchronized supersteps. Each active vertex reads incoming messages, updates its state, and sends messages that become available in the next superstep.

Global barriers simplify reasoning and checkpointing but allow a slow or overloaded worker to delay every other partition.

# References

[[bigdatamanagementandprocessing.pdf]]
