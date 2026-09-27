2026-09-21 22:12

Status: #baby

Tags: [[Object-Oriented Design Patterns]]

# Builder Pattern

The builder pattern separates the construction process for a complex object from the finished object's representation. A builder can collect or sequence required parts, validate that construction is complete, and then produce the object. This is useful when a constructor with many optional arguments obscures which combinations are valid, but it adds little when an object can be created clearly in one step.

A builder moves the steps required to assemble a complex object out of the client. Different builders can follow the same construction process while producing different representations, and a director can coordinate the sequence when that sequence itself is reusable.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

[[hands-ondesignpatternswithcandnetcore.pdf]]
