2026-09-08 21:16

Status: #baby

Tags: [[C Sharp Interfaces Generics and Inheritance]]

# C# Delegates

A C# delegate is a type-safe reference to a method with a specified parameter and return signature. Code can store the delegate, pass it as data, and invoke the referenced method later without depending directly on its declaring type.

Several compatible method references can be combined into a multicast delegate and invoked in sequence. Delegates form the basis of events and also appear as the function arguments used by LINQ operators and other callback-oriented APIs.

A delegate can be assigned any compatible static or instance method, including through method-group conversion. A multicast delegate maintains an invocation list that can be extended with `+=` and reduced with `-=`, invoking registered methods in order.

The target can be supplied as a named method, anonymous method, or lambda expression as long as its signature is compatible. This makes a delegate a uniform callback value even when the underlying behavior is declared in different syntactic forms.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

[[c80andnetcore30moderncross-platformdevelopment.pdf]]

[[programmingincexam70-483mcsdguide.pdf]]
