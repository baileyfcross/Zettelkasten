2026-11-11 18:27

Status: #baby

Tags: [[Structured and Modular Software Design]]

# Top-Down Decomposition

Top-down decomposition begins with a complete problem and divides it into smaller subproblems, then repeatedly refines one subproblem until its solution is sufficiently concrete to implement. A common first division separates input, computation, and output.

This method makes the planned control flow explicit and defers low-level decisions while the overall shape is being established. Its weakness is that data or representation knowledge may be shared across several sequential steps, so a change can cross the boundaries created by the control flow.

# References

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]

