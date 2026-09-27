2026-09-21 22:12

Status: #baby

Tags: [[Object-Oriented Design Patterns]] [[Xamarin Application Architecture]]

# Decorator Pattern

A decorator implements the same interface as an object it wraps, delegates the core operation to that object, and adds behavior around it. The book's message decorators change console color while leaving simple or alert message classes responsible for their own output. Wrapping can be composed or selected at runtime, extending behavior without requiring a subclass for every combination of features.

Decorator adds behavior by wrapping an object through a compatible interface, so the new responsibility can be composed at runtime without creating a subclass for every combination. The wrapper should preserve the wrapped object's established contract while adding its concern.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

[[hands-ondesignpatternswithcandnetcore.pdf]]

[[hands-onmobiledevelopmentwithnetcore.pdf]]
