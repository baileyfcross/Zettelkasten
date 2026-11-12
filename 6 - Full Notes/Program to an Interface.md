2026-11-11 18:27

Status: #baby

Tags: [[Software Design Principles]]

# Program to an Interface

Programming to an interface makes client code depend on a shared capability rather than one concrete implementation. Several shapes, storage mechanisms, or behaviors can then satisfy the same client contract without requiring a separate application for each concrete type.

The abstraction preserves flexibility only when it is cohesive. Expanding one interface with operations that most implementations do not use merely transfers concrete differences into a bloated contract and conflicts with the [[Interface Segregation Principle]].

# References

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]

