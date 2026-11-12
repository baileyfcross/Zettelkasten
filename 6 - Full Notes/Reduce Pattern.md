2026-11-11 18:27

Status: #baby

Tags: [[Parallel Program Design]]

# Reduce Pattern

The Reduce pattern combines a collection of partial values into a smaller result through a repeated operation. A tree-shaped reduction can combine pairs concurrently across levels, reducing elapsed depth when the operation supports a safe reassociation.

The combine rule must preserve the meaning of the serial calculation. Addition over exact integers is associative, but floating-point rounding or a stateful operation can make a different grouping produce a different result, so parallel reduction semantics must be chosen deliberately.

# References

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]

