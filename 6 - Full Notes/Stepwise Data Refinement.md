2026-11-11 18:27

Status: #baby

Tags: [[Structured and Modular Software Design]]

# Stepwise Data Refinement

Stepwise data refinement develops a program's representation alongside its procedural detail. When a task is divided into subtasks, the associated data description and interfaces are refined at the same level instead of being fixed prematurely.

The eight-queens example moves from an entire board to representations of occupied rows and diagonals, then considers a compact column-to-row array. Each representation changes the cost and clarity of checking a partial solution, showing that refining control without refining data leaves an essential design decision unresolved.

# References

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]

