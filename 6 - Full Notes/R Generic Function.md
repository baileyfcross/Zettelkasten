2026-10-07 17:18

Status: #baby

Tags: [[R Programming Environment]]

# R Generic Function

An R generic function represents an operation whose implementation depends on the class or signature of its arguments. The generic defines the common calling interface, while registered methods supply class-specific behavior.

In the formal S4 system, setGeneric establishes the operation and [[R Method Dispatch]] selects among implementations registered with setMethod. This separates the meaning of an operation such as summary or plotting from the internal representation of each participating class.

# References

[[statisticalcomputingincplusplusandr.pdf]]
