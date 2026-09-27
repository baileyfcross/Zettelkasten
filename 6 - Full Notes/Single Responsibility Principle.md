2026-09-21 22:12

Status: #baby

Tags: [[Software Design Principles]]

# Single Responsibility Principle

The single responsibility principle gives a class one coherent reason to change. When user interaction, business rules, and storage concerns all reside in one class, a change in any one area can disturb the others. Separating those responsibilities makes each component easier to understand and test, provided the split follows real change boundaries rather than producing many trivial wrappers.

One practical test is whether a class has more than one independent reason to change. When unrelated responsibilities share a class, modifying one concern can disturb dependencies belonging to the other and make the code harder to isolate.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

[[hands-ondesignpatternswithcandnetcore.pdf]]
