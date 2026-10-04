2026-09-08 21:16

Status: #baby

Tags: [[C Sharp Interfaces Generics and Inheritance]]

# C# Polymorphism and Overrides

Polymorphism lets code use a base-class or interface reference while runtime dispatch selects behavior supplied by the actual derived object. A base member marked virtual can be replaced by an override that preserves the same contract with specialized behavior.

Hiding a member creates a separate compile-time choice and is not the same as overriding it. Abstract members require derived implementations, while sealed types or members prevent further inheritance or overrides when an extension point would violate the design.

Polymorphism lets code invoke a common contract while the runtime type supplies the concrete behavior. Overriding inherited operations and implementing abstract members are dynamic forms; method or operator overloading chooses among statically known signatures.

That timing distinction prevents a common confusion: an overload is selected from the compile-time argument types, while an override is dispatched from the runtime object type. The two mechanisms can share a method name but solve different forms of variation.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

[[c80andnetcore30moderncross-platformdevelopment.pdf]]

[[programmingincexam70-483mcsdguide.pdf]]
