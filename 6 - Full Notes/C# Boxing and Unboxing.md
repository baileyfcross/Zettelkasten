2026-10-04 12:25

Status: #baby

Tags: [[C Sharp Operators Flow and Conversion]]

# C# Boxing and Unboxing

Boxing converts a value type into an `object` or compatible interface reference by placing a copy of the value in a managed object. Unboxing extracts the value through an explicit cast to its compatible value type.

The pair is type-safe but not free: boxing allocates and copies, while unboxing performs a runtime type check before copying the value out. A [[Generic Type]] can preserve the concrete type and avoid routine boxing when a reusable API would otherwise store values as `object`. This makes boxing distinct from ordinary C# casting and numeric conversion.

# References

[[programmingincexam70-483mcsdguide.pdf]]
