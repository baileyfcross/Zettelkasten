2026-09-16 00:09

Status: #baby

Tags: [[R Function Design]]

# Global Variable Side Effect

A global variable side effect occurs when a function reads or changes state outside its arguments and local environment. The behavior can make results depend on call history and complicate testing or reuse.

Passing required values as arguments and returning changes as results produces a clearer interface.

# References

[[essentialsofdatascience.pdf]]

