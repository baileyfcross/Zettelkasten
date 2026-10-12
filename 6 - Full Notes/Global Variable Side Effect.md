2026-09-16 00:09

Status: #baby

Tags: [[R Function Design]] · [[R Scripts Functions and Debugging]]

# Global Variable Side Effect

A global variable side effect occurs when a function reads or changes state outside its arguments and local environment. The behavior can make results depend on call history and complicate testing or reuse.

Passing required values as arguments and returning changes as results produces a clearer interface.

The book warns that a global object can change during a session and silently alter a function that reads it. Supplying that object through a [[Function Argument]] makes the dependency traceable during debugging and allows the same function to operate on different inputs safely.

# References

[[essentialsofdatascience.pdf]]

[[rstudentcompanion.pdf]]
