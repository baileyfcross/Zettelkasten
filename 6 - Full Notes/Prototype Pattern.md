2026-09-21 22:12

Status: #baby

Tags: [[Object-Oriented Design Patterns]]

# Prototype Pattern

The prototype pattern creates an object by copying an existing instance rather than selecting and invoking a concrete constructor at the call site. The source identifies it as a creational option for cloning. It is most useful when an already configured example captures a complex starting state; the copy contract must still make clear which nested values are duplicated and which remain shared.

The source emphasizes prototype as an alternative to reconstructing an object through its ordinary creation path: a configured instance is cloned, then treated as the starting point for another object. Correct use depends on defining which nested state is shared or copied.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

[[hands-ondesignpatternswithcandnetcore.pdf]]
