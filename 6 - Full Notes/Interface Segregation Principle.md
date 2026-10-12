2026-09-21 22:12

Status: #baby

Tags: [[Software Design Principles]]

# Interface Segregation Principle

The interface segregation principle keeps a contract focused on operations its consumers actually need. A read-only inventory command should depend on a read interface, while a command that changes quantity depends on a write interface; neither needs to see an unrelated method. Smaller role-specific interfaces reduce coupling and make tests and future refactoring more precise.

Small capability-focused interfaces prevent implementers from depending on or supplying members they do not need. A class can combine several applicable interfaces instead of inheriting one broad contract containing unrelated responsibilities.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

[[hands-ondesignpatternswithcandnetcore.pdf]]
