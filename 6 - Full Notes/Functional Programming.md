2026-09-21 22:12

Status: #baby

Tags: [[Functional Programming in C Sharp]]

# Functional Programming

Functional programming organizes computation around functions that transform values, emphasizing explicit inputs and results over hidden mutation. C# supports this style without requiring an entirely functional application: delegates and lambdas represent behavior, LINQ composes transformations, and pure calculations can be separated from database and user-interface effects. The benefit is that central business rules become easier to reason about and test when their dependencies are visible.

Under a strict functional interpretation, a function consumes inputs and produces outputs without changing the supplied data. Larger computations are built by feeding one result into other functions, making data flow explicit and contrasting with object-oriented designs that focus on constructing and changing objects.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

[[statisticalcomputingincplusplusandr.pdf]]
