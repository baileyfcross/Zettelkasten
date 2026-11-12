2026-11-11 18:27

Status: #baby

Tags: [[Software Construction and Refactoring]]

# Single-Purpose Function

A single-purpose function performs one coherent operation at one level of abstraction. Small focused functions isolate errors, expose reusable behavior, and require fewer distinct cases to test than a long routine that computes, formats, changes state, and reports status at once.

Line count is only a warning signal, but an unusually long function often contains several responsibilities. [[Extract Method Refactoring]] can give each responsibility a name and leave the original function as a readable statement of the larger sequence.

# References

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]

