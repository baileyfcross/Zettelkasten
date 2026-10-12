2026-10-07 17:18

Status: #baby

Tags: [[C++ Scientific Programming]]

# C++ Function Object

A C++ function object is an object whose call operator is overloaded so that the object can be invoked with function-call syntax. It can wrap a function pointer or store parameters and state needed by repeated evaluations.

Numerical routines can accept a function object as the objective to evaluate, separating the search algorithm from the mathematical function. This allows the same [[Golden Section Search]] or Newton routine to work with different objectives without hard-coding them into the optimizer.

# References

[[statisticalcomputingincplusplusandr.pdf]]
