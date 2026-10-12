2026-10-07 17:18

Status: #baby

Tags: [[C++ Scientific Programming]]

# C++ Scope

C++ scope determines the region in which a declared name can be used. A name declared inside a function or block has local scope, while a declaration outside every function has global scope and can be visible to multiple functions in the translation unit.

Narrow scope reduces unintended coupling because temporary state disappears when execution leaves its block. Global constants can avoid repeated calculation, but mutable global state makes numerical code harder to reason about and test.

# References

[[statisticalcomputingincplusplusandr.pdf]]
