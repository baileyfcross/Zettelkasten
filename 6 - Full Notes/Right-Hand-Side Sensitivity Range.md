2026-10-03 22:06

Status: #baby

Tags: [[Linear Programming Duality and Sensitivity]]

# Right-Hand-Side Sensitivity Range

A right-hand-side sensitivity range gives the interval over which one resource value may change while the current basis remains feasible and optimal. Multiplying the changed right-hand-side vector by the existing basis inverse produces the new basic-variable values.

The allowable interval is obtained by requiring all of those values to stay nonnegative. Within it, the existing dual variables determine the corresponding objective change; outside it, feasibility may need to be restored by the [[Dual Simplex Method]].

# References

[[optimizationusinglinearprogramming.pdf]]

