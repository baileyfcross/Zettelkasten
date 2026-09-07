2026-09-06 20:37

Status: #baby

Tags: [[Application Debugging]]

# Conditional Breakpoint

A conditional breakpoint pauses execution only when a specified expression or hit-count condition is satisfied. It is useful when a line runs many times but only one state or iteration is relevant to the fault.

The condition is evaluated when execution reaches the ordinary [[Breakpoint]] location. This reduces repeated manual continuation and preserves the state of the interesting case for inspection.

# References

[[aspnetcore3andangular9_3ed.pdf]]
