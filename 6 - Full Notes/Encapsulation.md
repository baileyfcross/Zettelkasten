2026-09-26 22:56

Status: #baby

Tags: [[C Sharp Object-Oriented Type Design]]

# Encapsulation

Encapsulation keeps an object's representation behind a controlled public surface. In C#, access modifiers can hide fields while properties and methods expose only the operations callers need.

The boundary protects invariants because outside code cannot freely place the object into every state its raw fields could represent. Encapsulation is therefore about assigning responsibility, not merely marking members `private`.

A class applies encapsulation by grouping state with the operations that interpret it and exposing only the necessary methods or properties. Callers depend on that stable surface while the class remains free to change how the state is represented internally.

In C++, private members are accessible only through the class's own methods and selected friends, protected members extend that access to derived classes, and public members form the external interface. A numerical class can therefore prevent callers from changing its dimensions or storage pointer without the checks required to preserve a valid object.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

[[programmingincexam70-483mcsdguide.pdf]]

[[statisticalcomputingincplusplusandr.pdf]]
