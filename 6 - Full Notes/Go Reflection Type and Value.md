2026-10-19 01:48

Status: #baby

Tags: [[Go Standard Library and Service Development]]

# Go Reflection Type and Value

Go reflection represents runtime type information with `reflect.Type` and a runtime value with `reflect.Value`. Code can inspect a value's kind, read it through the kind-appropriate accessor, and in allowed cases construct or modify data dynamically.

Reflection supports generic facilities such as formatting and serialization but cannot define new compiled Go types at runtime. Asking a reflected value for an incompatible representation can panic, so reflective code must check kinds and validity carefully.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
