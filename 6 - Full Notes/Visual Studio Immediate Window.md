2026-09-26 22:56

Status: #baby

Tags: [[Visual Studio Development Workflow]]

# Visual Studio Immediate Window

The Visual Studio Immediate window evaluates expressions and invokes methods in the context of a paused debugging session. It can inspect or temporarily change values and test what an operation returns at the current execution point.

Because evaluations can call code and mutate state, the window is not purely observational. Any change made there should be treated as part of the debugging experiment when interpreting later behavior.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

