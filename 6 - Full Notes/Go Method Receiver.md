2026-10-19 01:48

Status: #baby

Tags: [[Go Types Interfaces and Generics]]

# Go Method Receiver

A Go method is a function with a receiver declared before the method name. The receiver associates behavior with a named type while leaving the method body outside the type declaration.

A value receiver operates on a copy of the value, whereas a pointer receiver can mutate the original and avoids copying a large receiver. The chosen receiver form also determines the type's method set and therefore which interfaces the value or its pointer satisfies.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
