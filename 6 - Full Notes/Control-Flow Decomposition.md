2026-11-11 18:27

Status: #baby

Tags: [[Structured and Modular Software Design]]

# Control-Flow Decomposition

Control-flow decomposition organizes a program around the sequence of operations required to produce a result. A master routine invokes stages such as reading, transforming, sorting, and printing, while subordinate routines refine each stage.

The structure makes execution order easy to see, but it may leave common data accessible to many routines or require that data be passed through the sequence. When future changes concern a representation rather than the order of work, [[Change-Oriented Decomposition]] can contain them more effectively.

# References

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]

